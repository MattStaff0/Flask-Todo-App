#imports 
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

# Creating the app object
app = Flask(__name__)
Scss(app)

# configuring the app the use the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# making a class to be our model - row of data  
class Task(db.Model): 
    # each item is going to have an id - able to remove/update them 
    id = db.Column(db.Integer, primary_key=True )
    # the content of each item - content is a string limit of 100 chars
    content = db.Column(db.String(100), nullable=False)
    # is the task completed
    completed = db.Column(db.Integer)
    # date of the task created
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str: 
        return f"Task {self.id}"


# Making the index/home page to the app
@app.route("/", methods=["POST", "GET"])
def index():
    # adding a task 
    if request.method == "POST":
        # getting the content from the ID atr on the form in the index.html
        current_task = request.form['content']             # this is the info from the form in the index.html 
        new_task = Task(content=current_task)
        try:
            # adding the task
            db.session.add(new_task)
            #  committing the add to the database
            db.session.commit()
            # redirect the user back to the homescreen
            return redirect('/')
        except Exception as e:
            # catch and print error
            print(f'ERROR:{e}')
            return f'ERROR:{e}'
    # seeing all current task
    else:
        # gets all the tasks 
        tasks = Task.query.order_by(Task.created).all()
        # return the template with the tasks
        return render_template('index.html', tasks=tasks)

# delete an item 
@app.route("/delete/<int:id>")
def delete(id:int):
    # delete based on the primary key -> id
    delete_task = Task.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f'ERROR: {e}'


# edit an item
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id:int):
    # edit based on the primary key -> id
    task = Task.query.get_or_404(id)
    # if the request is a post to add
    if request.method == "POST":
        # update the context
        task.content = request.form['content']
        try:
            # commit the new updates
            db.session.commit()
            return redirect('/')
        # error handling
        except Exception as e:
            return f'ERROR: {e}'
    else:
        # need to render the new edit.html
        return render_template("edit.html", task=task)


if __name__ in "__main__":
    # making an app context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
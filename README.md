# Flask Todo App

A simple, clean todo application built with Flask and SQLAlchemy. This app allows users to create, edit, and delete tasks with a modern dark-themed interface.

## Features

- ✅ Add new tasks
- ✏️ Edit existing tasks
- 🗑️ Delete tasks
- 📅 Automatic timestamp creation
- 🌙 Dark mode interface
- 📱 Responsive design

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS (SCSS), Jinja2 templates
- **Styling**: Custom SCSS with dark theme
- **Additional**: Flask-SCSS for automatic SCSS compilation

## Project Structure

```
Flask-Todo-App/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── styles.scss       # SCSS source file
│   ├── styles.css        # Compiled CSS
│   └── styles.css.map    # CSS source map
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Main todo list page
│   └── edit.html         # Edit task page
├── instance/
│   └── database.db       # SQLite database (auto-generated)
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Flask-Todo-App
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   ```bash
   # On Windows
   env\Scripts\activate
   
   # On macOS/Linux
   source env/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

### Adding Tasks
1. Type your task in the input field at the bottom
2. Click "Add Task!" button
3. Your task will appear in the table above

### Editing Tasks
1. Click the "Edit" button next to any task
2. Modify the task content
3. Click "Update Task" to save changes

### Deleting Tasks
1. Click the "Delete" button next to any task
2. The task will be permanently removed

## Database Schema

The app uses a simple SQLite database with one table:

**Task Model:**
- `id` (Integer, Primary Key) - Unique identifier
- `content` (String, max 100 chars) - Task description
- `completed` (Integer) - Completion status (not currently used in UI)
- `created` (DateTime) - Timestamp when task was created

## API Endpoints

- `GET /` - Display all tasks and add new task form
- `POST /` - Create a new task
- `GET /edit/<id>` - Display edit form for specific task
- `POST /edit/<id>` - Update specific task
- `GET /delete/<id>` - Delete specific task

## Customization

### Styling
The app uses SCSS for styling. Main style file is located at `static/styles.scss`. Key design elements:

- **Color Scheme**: Dark theme with blue accents
- **Typography**: Clean, modern fonts
- **Layout**: Centered design with responsive table
- **Interactive Elements**: Hover effects and smooth transitions

### Color Variables (SCSS)
```scss
$background-color: #0f172a;  // Dark blue background
$text-color: #f1f5f9;        // Light gray text
$border-color: #334155;      // Medium gray borders
$accent-color: #8b5cf6;      // Purple accent
$button-color: #3b82f6;      // Blue buttons
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Future Enhancements

- [ ] Task completion toggle
- [ ] Task categories/tags
- [ ] Due dates
- [ ] Search functionality
- [ ] User authentication
- [ ] Export tasks to CSV/JSON
- [ ] Mobile app version

## Troubleshooting

**Database Issues:**
- If you encounter database errors, delete the `instance/database.db` file and restart the app

**SCSS Not Compiling:**
- Ensure Flask-SCSS is installed: `pip install Flask-SCSS`
- Check that your SCSS syntax is valid

**Port Already in Use:**
- Change the port by modifying the last line in `app.py`: `app.run(debug=True, port=5001)`

---

Built with ❤️ using Flask

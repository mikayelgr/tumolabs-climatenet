# Simple Flask Application

This is a simple Flask application that serves a static `index.html` file.

## Requirements

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Setup

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure the virtual environment is activated.

2. Run the Flask application:

   ```sh
   flask run --host=0.0.0.0
   ```

3. Open your web browser and navigate to `http://127.0.0.1:5000` to see the application in action.

## Project Structure

```
.
├── .gitignore
├── README.md
├── app.py
├── requirements.txt
└── static
    └── index.html
```

- `app.py`: The main Flask application file.
- `requirements.txt`: Lists the dependencies required to run the application.
- `static/index.html`: The static HTML file served by the Flask application.

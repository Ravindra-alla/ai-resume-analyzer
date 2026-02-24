# AI Resume Analyzer

A lightweight web application that processes uploaded resumes and extracts key information using AI-driven parsing.

## Features

- Upload resumes in supported formats
- Parse and analyze content for skills, experience, education, etc.
- Display results in a user-friendly interface

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Virtual environment (venv)

### Installation

```bash
# clone the repository
git clone <repo-url>
cd "AI BASED resume analyser"

# create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

### Running the App

```bash
python app.py
```

Visit http://localhost:5000 in your browser.

## Deployment

Refer to [deployment.md](deployment.md) for instructions, including Render-specific steps.

> **Note:** For production hosting (Render, Heroku, etc.) you’ll need a WSGI server like `gunicorn`. Make sure `gunicorn` is added to `requirements.txt` before deploying.

## Project Structure

- `app.py` &mdash; Flask application entry point
- `resume_parser.py`, `matcher.py` &mdash; core parsing logic
- `templates/` &mdash; HTML pages
- `static/` &mdash; CSS and JavaScript
- `uploads/` &mdash; directory for uploaded files

## Contributing

Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

---
*Generated on 2026-02-24*
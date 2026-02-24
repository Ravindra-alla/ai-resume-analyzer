# Deployment Instructions

This document outlines steps to deploy the AI Resume Analyzer application.

## Prerequisites

- Python 3.8+ installed
- Virtual environment tool (venv or virtualenv)
- Git (optional for pulling source)

## Setup

1. Clone the repository or ensure you have the project files locally.

```bash
cd "c:\Users\ALLA NAGA RAVINDRA\Desktop\AI BASED resume analyser"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure any environment variables (e.g., secret keys) if needed.

## Running Locally

```bash
python app.py
```

The application starts on http://localhost:5000 by default.

## Production Deployment

1. Choose a hosting platform (e.g., Azure App Service, AWS Elastic Beanstalk, Heroku, Render).
2. Configure the environment and install dependencies via `requirements.txt`.
3. Use a production-ready server (Gunicorn, uWSGI) behind a web server if necessary.
4. Set environment variables and upload necessary static files.

### Deploying on Render

Render is a simple platform to host Python applications. Follow these steps:

1. **Create a Render account** or sign in at https://render.com.
2. Click **New** → **Web Service**.
3. Connect your GitHub/GitLab account and select the `ai-resume-analyzer` repository.
4. Choose **Python** as the runtime.
5. Set the **Build Command** to:
   ```bash
   pip install -r requirements.txt
   ```
6. Set the **Start Command** to:
   ```bash
   gunicorn app:app
   ```
   (ensure `gunicorn` is listed in `requirements.txt`)
7. Add any required environment variables in the **Environment** section (e.g., `SECRET_KEY`).
8. Click **Create Web Service**. Render will build and deploy the app automatically.
9. Once deployed, your app will be available at the provided Render URL.

Render handles SSL, scaling, and background workers if needed.

## Additional Notes

- Ensure file upload directory (`uploads/`) is writable.
- Logs can be configured in `app.py`.

---
*Generated on 2026-02-24*
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from resume_parser import extract_text_from_pdf, clean_text
from matcher import calculate_match, get_missing_skills

app = Flask(__name__)

# Config
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return render_template('index.html', error="No resume file uploaded")

    file = request.files['resume']
    job_description = request.form.get('job_description', '').strip()

    if file.filename == '':
        return render_template('index.html', error="No file selected")

    if not allowed_file(file.filename):
        return render_template('index.html', error="Only PDF files are allowed")

    filename = secure_filename(file.filename)
    if not filename:
        filename = "resume.pdf"

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Extract resume text
    resume_text = extract_text_from_pdf(file_path)
    if not resume_text:
        return render_template(
            'index.html',
            error="Could not extract text. Please upload a text-based PDF."
        )

    # Clean text
    cleaned_resume = clean_text(resume_text)
    cleaned_job_desc = clean_text(job_description)

    # Match calculation
    match_percentage = calculate_match(cleaned_resume, cleaned_job_desc)
    missing_skills, common_keywords = get_missing_skills(
        cleaned_resume, cleaned_job_desc
    )

    return render_template(
        'result.html',
        match_percentage=match_percentage,
        missing_skills=missing_skills,
        common_keywords=common_keywords
    )


if __name__ == '__main__':
    app.run(debug=True)

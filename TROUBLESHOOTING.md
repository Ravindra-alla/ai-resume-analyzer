# Troubleshooting Guide

## Common Issues

### 1. `ModuleNotFoundError: No module named ...`
**Issue:** The required Python libraries are not installed.
**Fix:** Run the following command in your terminal:
```bash
pip install -r requirements.txt
```

### 2. `AttributeError: module 'PyPDF2' has no attribute 'PdfReader'`
**Issue:** You might have an old version of PyPDF2.
**Fix:** Upgrade PyPDF2:
```bash
pip install --upgrade PyPDF2
```

### 3. Application crashes on upload
**Issue:** The PDF might be an image-based PDF (scanned) or encrypted.
**Fix:** This basic analyzer only supports text-based PDFs. Try converting your resume to a standard text PDF.

### 4. Zero match percentage
**Issue:** It's possible the resume parser couldn't extract text, or the job description is vastly different.
**Fix:** Copy text directly from your PDF and paste it into the job description box to test if the tokenizer sees it.

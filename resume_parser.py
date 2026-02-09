import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
    return text

def clean_text(text):
    """
    Cleans the extracted text: removes special characters and extra spaces.
    """
    # Keep alphanumeric, spaces, and specific special characters for skills (., +, #, -)
    text = re.sub(r'[^a-zA-Z0-9\s\.\+\#\-]', '', text)
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    return text.lower().strip()

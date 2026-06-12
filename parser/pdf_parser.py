import pdfplumber

def extract_pdf_text(pdf_file):
    text = ""

    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        text = f"Error reading PDF: {str(e)}"

    return text
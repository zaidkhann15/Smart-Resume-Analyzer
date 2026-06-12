from docx import Document

def extract_docx_text(docx_file):
    text = ""

    try:
        doc = Document(docx_file)

        for para in doc.paragraphs:
            text += para.text + "\n"

    except Exception as e:
        text = f"Error reading DOCX: {str(e)}"

    return text
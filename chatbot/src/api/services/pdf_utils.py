import fitz


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extrai texto de um PDF em bytes.
    """
    pdf = fitz.open(stream=file_bytes, filetype="pdf")
    return "\n".join([page.get_text() for page in pdf])

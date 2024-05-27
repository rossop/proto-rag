import PyPDF2
from typing import List, Dict


def parse_pdf_with_metadata(file_path: str) -> List[Dict[str, str]]:
    """Parses a PDF file and extracts text along with metadata from each page.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        List[Dict[str, str]]: List of dictionaries, each containing the text and metadata of a page.
    """
    pdf_data = []
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            pdf_data.append({
                "text": text,
                "page_number": page_num + 1
            })
    return pdf_data

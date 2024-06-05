import os
import PyPDF2
from typing import List, Dict, Any


def parse_pdf_with_metadata(file_path: str) -> List[Dict[str, Any]]:
    """Parses a PDF file and extracts text along with metadata from each page.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        List[Dict[str, str]]: List of dictionaries, each containing the text and metadata of a page.
    """
    pdf_data = []
    pdf_name = os.path.basename(file_path)
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            pdf_data.append({
                "text": text,
                "page_number": page_num + 1,
                "pdf_name": pdf_name
            })
    return pdf_data

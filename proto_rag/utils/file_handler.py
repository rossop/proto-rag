import os
from typing import List, Dict, Any
from .pdf_parser import parse_pdf_with_metadata
from .text_chunker import chunk_text_with_metadata
from .neo4j_handler import save_data_to_neo4j

def process_pdfs_with_metadata(pdf_files: List[str], neo4j_session) -> Dict[str, List[Dict[str, Any]]]:
    """Processes a list of PDF files, chunking their text with metadata and saving the chunks to Neo4j.

    Args:
        pdf_files (List[str]): List of PDF file paths.
        neo4j_session: Neo4j database session.

    Returns:
        Dict[str, List[Dict[str, Any]]]: Dictionary with PDF file names as keys and list of text chunks with metadata as values.
    """
    pdf_data = {}
    for pdf_file in pdf_files:
        pdf_name = os.path.basename(pdf_file)
        print(f"Parsing {pdf_name}")
        pages = parse_pdf_with_metadata(pdf_file)
        all_chunks = chunk_text_with_metadata(pages, chunk_size=500)
        pdf_data[pdf_name] = all_chunks
        save_data_to_neo4j(neo4j_session, all_chunks)
    return pdf_data
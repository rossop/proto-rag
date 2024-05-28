from typing import List, Dict, Any

def chunk_text_with_metadata(pdf_pages: List[Dict[str, Any]], chunk_size: int = 500) -> List[Dict[str, Any]]:
    """Chunks the given PDF text into smaller pieces and attaches metadata for each page.

    Args:
        pdf_pages (List[Dict[str, Any]]): The list of PDF data with text and metadata for each page.
        chunk_size (int, optional): The size of each chunk. Defaults to 500.

    Returns:
        List[Dict[str, Any]]: List of dictionaries, each containing a text chunk and its metadata.
    """
    chunks = []
    for pdf in pdf_pages:
        chunk_seq_id = 0
        text = pdf["text"]
        metadata = {key: pdf[key] for key in pdf if key != "text"}

        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]
            chunk_metadata = metadata.copy()
            chunk_metadata.update({
                "chunk_text": chunk,
                "chunk_seq_id": chunk_seq_id
            })
            chunks.append(chunk_metadata)
            chunk_seq_id += 1
    return chunks

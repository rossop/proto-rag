import pytest
from proto_rag.utils.text_chunker import chunk_text_with_metadata

@pytest.mark.parametrize("pdf_pages, chunk_size", [
    ([{"text": "This is a sample text for chunking.", "page_number": 1, "pdf_name": "sample1.pdf"}], 10),
    ([{"text": "Another example text to be chunked into pieces.", "page_number": 2, "pdf_name": "sample2.pdf"}], 15)
])
def test_chunk_text_with_metadata(pdf_pages, chunk_size):
    chunks = chunk_text_with_metadata(pdf_pages, chunk_size)
    assert isinstance(chunks, list)
    assert all(isinstance(chunk, dict) for chunk in chunks)
    assert all("chunk_text" in chunk and "chunk_seq_id" in chunk for chunk in chunks)
    assert all(chunk["chunk_seq_id"] < len(chunks) for chunk in chunks)

if __name__ == "__main__":
    pytest.main()

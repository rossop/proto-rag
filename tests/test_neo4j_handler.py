import os
import pytest
from unittest.mock import MagicMock
from proto_rag.utils.neo4j_handler import connect_to_neo4j
from proto_rag.utils.neo4j_handler import save_data_to_neo4j
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()

@pytest.mark.local_only
@pytest.mark.skipif(os.getenv('CI') == 'true', reason="Skip on CI")
def test_connect_to_neo4j():
    uri = os.getenv("NEO4J_URI")
    user = os.getenv("NEO4J_USER")
    password = os.getenv("NEO4J_PASSWORD")
    session = connect_to_neo4j(uri, user, password)
    assert session is not None
    session.close()



@pytest.mark.local_only
@pytest.mark.skipif(os.getenv('CI') == 'true', reason="Skip on CI")


def test_save_data_to_neo4j():
    session = MagicMock()
    
    chunks: List[Dict[str, Any]] = [
        {"chunk_text": "This is a sample text.", "page_number": 1, "pdf_name": "sample1.pdf", "chunk_seq_id": 0},
        {"chunk_text": "Another example text.", "page_number": 2, "pdf_name": "sample2.pdf", "chunk_seq_id": 1}
    ]
    
    save_data_to_neo4j(session, chunks)
    
    assert session.run.called
    assert session.run.call_count == len(chunks)
    for call, chunk in zip(session.run.call_args_list, chunks):
        args, kwargs = call
        assert args[0] == (
            """
            CREATE (n:Chunk {
                pdf_name: $pdf_name,
                page_number: $page_number,
                chunk_seq_id: $chunk_seq_id,
                chunk_text: $chunk_text,
                form_id: $form_id
            })
            """
        )
        assert kwargs["pdf_name"] == chunk["pdf_name"]
        assert kwargs["page_number"] == chunk["page_number"]
        assert kwargs["chunk_seq_id"] == chunk["chunk_seq_id"]
        assert kwargs["chunk_text"] == chunk["chunk_text"]
        assert kwargs["form_id"] == chunk["pdf_name"].split('.')[0]

if __name__ == "__main__":
    pytest.main()


if __name__ == "__main__":
    pytest.main()


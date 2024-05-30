from neo4j import GraphDatabase
from typing import List, Dict, Any

def connect_to_neo4j(uri: str, user: str, password: str):
    """Connects to the Neo4j database.

    Args:
        uri (str): URI for the Neo4j database.
        user (str): Username for the Neo4j database.
        password (str): Password for the Neo4j database.

    Returns:
        Any: Neo4j session object.
    """
    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver.session()


def save_data_to_neo4j(session, chunks: List[Dict[str, Any]]) -> None:
    """Saves chunked data with metadata to the Neo4j database.

    Args:
        session: Neo4j database session.
        chunks (List[Dict[str, Any]]): List of dictionaries, each containing a text chunk and its metadata.
    """
    for chunk in chunks:
        session.run(
            """
            CREATE (n:Chunk {
                pdf_name: $pdf_name,
                page_number: $page_number,
                chunk_seq_id: $chunk_seq_id,
                chunk_text: $chunk_text,
                form_id: $form_id
            })
            """,
            pdf_name=chunk["pdf_name"],
            page_number=chunk["page_number"],
            chunk_seq_id=chunk["chunk_seq_id"],
            chunk_text=chunk["chunk_text"],
            form_id=chunk["pdf_name"].split('.')[0]  # Assuming form_id is derived from the pdf_name
        )

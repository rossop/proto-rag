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
    """Saves chunked data with metadata to the Neo4j database, merging chunks and creating Page and Document nodes.

    Args:
        session: Neo4j database session.
        chunks (List[Dict[str, Any]]): List of dictionaries, each containing a text chunk and its metadata.
    """
    prev_chunk_id = None
    for chunk in chunks:
        chunk_id = f"{chunk['pdf_name']}_p{chunk['page_number']}_c{chunk['chunk_seq_id']}"
        session.run(
            """
            MERGE (d:Document {name: $pdf_name, form_id: $form_id})
            MERGE (p:Page {pdf_name: $pdf_name, page_number: $page_number})
            MERGE (n:Chunk {chunk_id: $chunk_id, pdf_name: $pdf_name, page_number: $page_number, chunk_seq_id: $chunk_seq_id})
            SET n.chunk_text = $chunk_text
            MERGE (d)-[:HAS_PAGE]->(p)
            MERGE (p)-[:HAS_CHUNK]->(n)
            """,
            pdf_name=chunk["pdf_name"],
            page_number=chunk["page_number"],
            chunk_seq_id=chunk["chunk_seq_id"],
            chunk_text=chunk["chunk_text"],
            form_id=chunk["pdf_name"].split('.')[0],
            chunk_id=chunk_id
        )

        if prev_chunk_id and chunk["page_number"] == prev_page_number:
            session.run(
                """
                MATCH (prev:Chunk {chunk_id: $prev_chunk_id}), (curr:Chunk {chunk_id: $curr_chunk_id})
                MERGE (prev)-[:FOLLOWS]->(curr)
                """,
                prev_chunk_id=prev_chunk_id,
                curr_chunk_id=chunk_id
            )

        prev_chunk_id = chunk_id
        prev_page_number = chunk["page_number"]
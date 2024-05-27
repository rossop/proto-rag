from neo4j import GraphDatabase

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



import pytest
from proto_rag.utils.neo4j_handler import connect_to_neo4j
from dotenv import load_dotenv
import os

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

if __name__ == "__main__":
    pytest.main()

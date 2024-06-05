from dotenv import load_dotenv
import os
from neo4j import GraphDatabase
import time

# Load environment variables
load_dotenv()

# Get credentials from environment variables
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Function to create and delete a node
def create_and_delete_node():
    # Connect to Neo4j
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    session = driver.session()
    
    try:
        # Create a node
        create_query = "CREATE (n:TestNode {name: 'Temporary Node'}) RETURN n"
        session.run(create_query)
        print("Node created.")
        
        # Wait for 5 seconds
        time.sleep(5)
        
        # Delete the node
        delete_query = "MATCH (n:TestNode {name: 'Temporary Node'}) DELETE n"
        session.run(delete_query)
        print("Node deleted.")
        
    finally:
        # Close the session
        session.close()
        driver.close()
        print("Session closed.")

if __name__ == "__main__":
    create_and_delete_node()

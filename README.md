# Proto-RAG: Retrieval-Augmented Generation with Neo4j and OpenAI

Proto-RAG is a Retrieval-Augmented Generation (RAG) system that integrates Neo4j as a knowledge graph and OpenAI's GPT-3.5 to provide intelligent responses based on the data stored in the knowledge graph. This project utilizes LangChain to facilitate the interaction between the knowledge graph and the language model.

## Features

- **Knowledge Graph Integration**: Utilizes Neo4j to store and query data.
- **Natural Language Processing**: Uses OpenAI's GPT-3.5 for generating responses.
- **Dynamic Cypher Query Generation**: Converts natural language questions into Cypher queries to fetch relevant data from Neo4j.
- **Interactive Command-Line Interface**: Allows users to ask questions and get responses interactively.
- **PDF Parsing**: Extract text from PDF files.
- **Text Chunking with Metadata**: Split text into manageable chunks and attach metadata.
- **JSON Saving**: Save parsed and chunked text into JSON files.
- **RAG Pipeline**: Retrieve data from Neo4j and generate summaries using OpenAI.

## Project Structure

```
proto-rag/
│
├── 📂 .github/workflows/
├── 📂 notebooks/
├── 📂 tests/
├── 📂 proto_rag/
│   ├── 📄 __init__.py
│   ├──  📂 utils/
│   │   ├── 📄 __init__.py
│   │   ├── 📄 pdf_parser.py
│   │   ├── 📄 text_chunker.py
│   │   ├── 📄 json_saver.py
│   │   ├── 📄 file_handler.py
│   │   ├── 📄 neo4j_handler.py
│   │   ├── 📄 openai_handler.py
│   │   └── 📄 rag_handler.py
│   └── 📄 main.py
├── 📄 .env                                 (UNTRACKED)
├── 📄 requirements.txt
├── 📂 venv/
├── 📄 Dockerfile (to be implemented)
├── 📄 .gitignore
```

## Getting Started

### Prerequisites

- Python 3.8+
- Neo4j Database
- OpenAI API Key

See `requirements.txt`.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/proto-rag.git
   cd proto-rag
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory with the following content:
   ```ini
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=your_neo4j_password
   OPENAI_API_KEY=your_openai_api_key
   ```

### Usage

1. **Start Neo4j**:
   Ensure your Neo4j database is running.

2. **Run the Main Script**:
   ```bash
   python -m proto_rag.main
   ```

3. **Interact with the System**:
   You can now ask questions related to the data stored in your Neo4j knowledge graph. For example:
   ```
   > What is CAD?
   ```

Utility functions to populate to parse PDFs and populate you graphs are also available.
<!-- - Parses PDFs listed in `pdf_files`.
- Chunks the parsed text with metadata.
- Saves the chunked text to a JSON file.
- Stores the chunked text in a Neo4j database.
- Retrieves data from Neo4j and generates summaries using OpenAI. -->


### Example

To add a new PDF for processing, add its path to the `pdf_files` list in `main.py`:
```python
pdf_files = [
    '/path/to/your/pdf1.pdf',
    '/path/to/your/pdf2.pdf',
    # Add more PDFs here
]
```

### Testing

Tests are written using `pytest`. To run the tests, execute:
```sh
pytest tests/
```

## Directory and File Responsibilities

- **`proto_rag/utils`**: Contains utility modules for PDF parsing, text chunking, JSON saving, Neo4j handling, OpenAI integration, and RAG implementation.
- **`proto_rag/main.py`**: Main script to run the entire pipeline.
- **`.env`**: Environment variables configuration file.
- **`requirements.txt`**: List of dependencies.
- **`Dockerfile`**: To be implemented for containerization.
- **`proto_rag/main.py`**: The main entry point of the application.
- **`proto_rag/utils/rag_handler.py**: Contains the logic for interacting with Neo4j and OpenAI.
- **`proto_rag/utils/__init__.py`**: Initializes the utils module.


## License

This project is licensed under the MIT License.



## Future Enhancements

### To-Do List

1. **Testing**:
    - Add unit tests for all utility functions.
    - Write integration tests to ensure modules work together correctly.
    - Develop end-to-end tests to verify the entire workflow.

2. **CI/CD**:
    - Set up continuous integration using GitHub Actions.
    - Automate testing and deployment processes.
    - Implement code quality checks (linting, formatting).

3. **Dockerization**:
    - Create a Dockerfile for containerization.
    - Build and test Docker images locally.
    - Deploy Docker containers using a container orchestration tool (e.g., Kubernetes).


## References

- [Neo4j](https://neo4j.com/)
- [OpenAI](https://www.openai.com/)
- [LangChain](https://github.com/langchain-ai/langchain)


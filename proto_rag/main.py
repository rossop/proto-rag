from utils.rag_handler import query_rag

def main():
    while True:
        question = input("> ")
        response = query_rag(question)
        print(f"Response: {response}")

if __name__ == "__main__":
    main()

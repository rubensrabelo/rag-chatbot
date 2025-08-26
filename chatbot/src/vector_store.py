from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def create_chroma_store(text: str, persist_dir: str = "./chroma_db"):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_texts(chunks, embedding=embeddings, persist_directory=persist_dir)
    return db


def get_context(db, question: str, k: int = 4) -> str:
    docs = db.similarity_search(question, k=k)
    return "\n".join([doc.page_content for doc in docs])
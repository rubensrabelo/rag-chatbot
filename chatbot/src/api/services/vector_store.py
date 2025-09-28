from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def create_chroma_store(text: str, persist_dir: str = "./chroma_db"):
    """
    Cria uma base vetorial Chroma a partir de um texto bruto.
    O texto é dividido em chunks com sobreposição, convertido em embeddings
    usando o modelo HuggingFace, e armazenado em uma base persistente.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = Chroma.from_texts(
        chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    return db


def get_context(db, question: str, k: int = 4) -> str:
    """
    Recupera contexto relevante da base vetorial com
    base em uma pergunta. Realiza uma busca semântica
    na base Chroma e retorna os conteúdos mais similares.
    """
    docs = db.similarity_search(question, k=k)
    return "\n".join([doc.page_content for doc in docs])

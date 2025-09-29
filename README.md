# RAG Chatbot com FastAPI, LangChain e React

Este projeto é uma API inteligente baseada em **RAG (Retrieval-Augmented Generation)**, construída com **FastAPI**, **LangChain** e integrada com um frontend em **React**. O objetivo é criar um chatbot capaz de responder perguntas com base em documentos enviados pelo usuário, utilizando modelos de linguagem do Hugging Face.

---

## Funcionalidades

- **Chat com RAG**: Respostas contextualizadas com base em documentos e histórico de conversa.
- **Upload de documentos**: Suporte para `.pdf`.

---

## Tecnologias Utilizadas

| Camada        | Ferramentas                          |
|---------------|--------------------------------------|
| Backend       | FastAPI, LangChain, Chroma, SQLite   |
| Frontend      | React (em desenvolvimento)           |
| Embeddings    | Hugging Face Embeddings              |
| Vetor Store   | ChromaDB                             |
| Ambiente      | Gerenciado com `uv` (super rápido!)  |

---

## Instalação com `uv` (Windows)

```bash
# Instalar uv (se necessário)
pip install uv

# Criar ambiente virtual
uv venv .venv
.venv\Scripts\activate

# Inicializar projeto
uv init

# Instalar dependências
uv add pyproject.toml
```

---

## Estrutura do Projeto

```

```

---

## Como rodar

```bash
uvicorn main:app --reload
```

Acesse a API em `http://localhost:8000` e interaja com os endpoints via Swagger ou seu frontend em React.

---

## Melhorias Futuras


---

## Créditos

Este projeto foi inspirado no tutorial da [FutureSmart AI sobre RAG com FastAPI e LangChain](https://blog.futuresmart.ai/building-a-production-ready-rag-chatbot-with-fastapi-and-langchain?source=more_series_bottom_blogs).

---

# RAG Chatbot · FastAPI + LangChain + React

API inteligente baseada em **RAG (Retrieval-Augmented Generation)**, construída com **FastAPI** e **LangChain**, integrada a um frontend em **React**.
Permite criar um chatbot capaz de responder perguntas com base em documentos enviados pelo usuário, utilizando modelos de linguagem do **Hugging Face**.

---

## Estrutura do Projeto

```bash
rag-chatbot/
├── README.md              # Visão geral do projeto
├── chatbot/               # Código do backend (FastAPI + LangChain)
├── frontend/              # Código do frontend (React)
└── docs/
    ├── roadmap.md         # Roadmap do projeto (backend + frontend)
    ├── next_steps.md      # Próximas tarefas detalhadas
    ├── session_logs.md    # Diário de desenvolvimento
    └── references.md      # Links e materiais úteis
```

---

## Documentação

Toda a documentação do sistema está centralizada na pasta [`docs/`](docs/), abrangendo **backend e frontend**:

* [Roadmap](docs/roadmap.md) – objetivos gerais e fases do projeto
* [Próximos Passos](docs/next_steps.md) – tarefas detalhadas e prioridades
* [Logs de Desenvolvimento](docs/session_logs.md) – histórico das sessões de trabalho
* [Referências](docs/references.md) – links, tutoriais e materiais de apoio

---

## Tecnologias Utilizadas

| Camada         | Ferramentas / Frameworks    |
| -------------- | --------------------------- |
| Backend        | FastAPI, LangChain          |
| Frontend       | React                       |
| Embeddings     | Hugging Face models         |
| Banco de Dados | ChromaDB, SQLite (ou outro) |

---
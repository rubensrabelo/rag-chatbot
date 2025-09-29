# RAG Chatbot · Backend (FastAPI + LangChain)

Backend do chatbot baseado em **RAG (Retrieval-Augmented Generation)**, construído com **FastAPI** e **LangChain**, integrado a um frontend em **React**.


---

## Estrutura do Backend

```bash
chatbot/
├── src/
│   ├── api/              
│   │   ├── routes/       # Definição das rotas/endpoints da API
│   │   ├── services/     # Lógica de negócio e integração com modelos
│   │   ├── state/        # Gerenciamento de estado, memória ou cache
│   │   └── utils/        # Funções utilitárias usadas pelos endpoints
│   ├── config/           # Configurações do projeto (variáveis, settings)
│   ├── db/               # Conexão e operações com o banco de dados
│   ├── logging_utils/    # Funções de logging e monitoramento
│   ├── models/           # Modelos de dados (ORM)
│   ├── schemas/          # Schemas Pydantic para validação de dados
│   ├── .env-example      # Exemplo de variáveis de ambiente
│   ├── chat.db           # Banco de dados SQLite local
│   └── main.py           # Ponto de entrada da aplicação
├── .gitignore            
├── .python-version       
├── pyproject.toml        
├── README.md             
└── uv.lock               
```

---

## Tecnologias

| Camada     | Ferramentas / Frameworks    |
| ---------- | --------------------------- |
| Backend    | FastAPI, LangChain          |
| Embeddings | Hugging Face Models         |
| Banco      | ChromaDB, SQLite (ou outro) |


---

## Como Rodar

### Clonar o repositório

```bash
git clone https://github.com/seu-usuario/rag-chatbot.git
cd rag-chatbot
```

### Criar e ativar ambiente virtual com `uv`

```bash
# Instalar uv caso não tenha
pip install uv

# Criar ambiente virtual e ativar
uv venv .venv
# No Windows
.venv\Scripts\activate
# No macOS/Linux
source .venv/bin/activate
```

### Instalar dependências do projeto

```bash
uv add pyproject.toml 
```

### Rodar o backend

```bash
cd ./src/

uvicorn main:app --reload
```

* API disponível em: [http://localhost:8000](http://localhost:8000)
* Documentação interativa: [http://localhost:8000/docs](http://localhost:8000/docs)
* Frontend: em desenvolvimento (ver pasta `frontend/`)
---


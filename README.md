# FinInsight AI

A FastAPI-based personal finance analytics backend that stores transactions in PostgreSQL and exposes endpoints for transaction management and conversational analysis.

## Project structure

- `main.py` - FastAPI app entrypoint
- `database.py` - SQLAlchemy engine, session, and base model configuration
- `models/transaction.py` - SQLAlchemy ORM model for transaction data
- `schemas/transaction.py` - Pydantic request schema for transactions
- `schemas/message.py` - Pydantic request schema for chat messages
- `routes/transaction.py` - Transaction-related API routes
- `routes/chat.py` - Chat/AI analysis API route
- `services/transaction_service.py` - Transaction query and aggregation logic
- `services/ai_service.py` - AI/NLP logic for intent extraction and analysis

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the environment:
   - Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - Command Prompt:
     ```cmd
     .\venv\Scripts\activate.bat
     ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
   ```
4. Configure PostgreSQL connection in `database.py` if needed.

## Database

The app uses PostgreSQL via SQLAlchemy. Update the connection string in `database.py`:

```python
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/fininsight"
```

The tables are created automatically when the app starts.

## API Endpoints

### Transactions

- `POST /transactions/`
  - Add a transaction
  - Request body: `amount`, `category`, `date`
- `GET /transactions/`
  - Retrieve all transactions
- `POST /transactions/upload`
  - Upload a CSV file of transactions
  - CSV columns: `amount`, `category`, `date`

### Chat Analytics

- `POST /chats/{chat_id}/messages`
  - Analyze user queries against transaction data
  - Request body: `content`
  - Returns intent, category breakdown, and AI analysis

## Running the app

Start the server with:

```bash
uvicorn main:app --reload
```

Then open your browser at `http://127.0.0.1:8000/docs` for the Swagger UI.

## Notes

- `main.py` currently imports some modules twice; this can be cleaned up.
- Keep this document updated as you add new routes, services, or external dependencies.

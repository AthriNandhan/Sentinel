# Sentinel-Code

Automated vulnerability remediation system using FastAPI, LangGraph, and Agentic AI.

## Prerequisities

- Python 3.10+
- Docker (for sandbox execution)

## Setup

1.  **Clone repository** (if applicable)
2.  **Navigate to backend directory**:
    ```bash
    cd sentinel_code/backend
    ```
3.  **Create virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Verification Script

Once dependencies are installed, you can verify the core workflow logic:

```bash
python ../../verify_setup.py
```

## Running the Backend

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.
API documentation is at `http://localhost:8000/docs`.

## Project Structure

- `app/agents`: Agent implementations (Red, Blue, Green)
- `app/graph`: LangGraph workflow definition
- `app/models`: Shared state models (Pydantic)
- `app/services`: External services (Sandbox, Logger)
- `app/api`: FastAPI routes

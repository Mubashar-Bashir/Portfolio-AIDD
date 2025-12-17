# Backend Setup

## Virtual Environment

To set up the Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Backend

```bash
cd backend
source ../venv/bin/activate
uvicorn main:app --reload
```
python3 -m venv venv
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
uvicorn app.main:app --reload
curl http://0.0.0.0:8000/api/users
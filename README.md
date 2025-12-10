
Analises Esportivas Pro - Scaffold Build
---------------------------------------
This scaffold includes:
- api/ (FastAPI backend)
- engine/ (AI & bet builder stubs)
- services/ (supabase/accounts stubs)
- frontend/ (Next.js and Vite scaffolds)
- mobile/ (flutter placeholder)
- Dockerfile and start.sh for deployment (uses api.main as entrypoint)

How to run (local, backend only):
1. pip install -r requirements.txt
2. uvicorn api.main:app --reload --port 8080

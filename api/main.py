
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from engine.abcde_engine import ai_generate_ticket, place_demo_bet, cleanup_old_demo

app = FastAPI(title="Analises Esportivas PRO API (Scaffold)")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root():
    return {"status":"online","time": datetime.utcnow().isoformat()}

@app.get("/api/health")
def health():
    return {"status":"ok","service":"analises-esportivas-pro"}

@app.post("/api/ai/generate")
def gen(matches: list):
    return ai_generate_ticket(matches)

@app.post("/api/bet/demo")
def bet_demo(account_id: str, payload: dict):
    return place_demo_bet(account_id, payload)

@app.delete("/api/cleanup")
def cleanup():
    return cleanup_old_demo()

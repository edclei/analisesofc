
import os
from datetime import datetime, timedelta

def place_demo_bet(account_id: str, payload: dict):
    bet = {
        "account_id": account_id,
        "selections": payload.get("selections"),
        "combined_odd": payload.get("combined_odd"),
        "prob": payload.get("prob"),
        "timestamp": datetime.utcnow().isoformat(),
        "status": "pending"
    }
    # placeholder: save to DB (supabase)
    return {"status":"DEMO_PLACED","bet":bet}

def ai_generate_ticket(matches: list):
    ticket = []
    for m in matches:
        patterns = []
        if m.get('goals_avg',0) > 1.0: patterns.append('+0.5 gols')
        if m.get('win_prob',0) > 0.6: patterns.append('time vence')
        ticket.append({"match": m.get('id'), "patterns": patterns})
    return {"ticket": ticket}

def cleanup_old_demo():
    return {"cleanup":"ok"}

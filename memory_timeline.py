# memory_timeline module
import requests

def run(_: str = None) -> dict:
    """
    Retrieve memory logs and organize by date and type.
    """
    try:
        response = requests.post(
            "https://core-builder-v-2-jamesrickstinso.replit.app/api/modules/memory_core/run",
            json={"payload": {"action": "retrieve"}}
        )
        logs = response.json().get("results", [])
    except Exception as e:
        return {"error": str(e)}

    timeline = {}
    for log in logs:
        date = log['timestamp'].split('T')[0]
        if date not in timeline:
            timeline[date] = []
        timeline[date].append({
            "type": log["type"],
            "context": log["context"],
            "content": log["content"],
            "timestamp": log["timestamp"]
        })

    return {"timeline": timeline, "count": len(logs)}
import json
from pathlib import Path

def load_conversations_json(base_path: Path):
    json_files = list(base_path.rglob("*.json"))
    
    if not json_files:
        print("❌ Keine JSON-Dateien gefunden.")
        return {}

    print(f"🔍 Gefundene JSON-Dateien: {len(json_files)}")
    
    result = {}
    for f in json_files:
        try:
            with open(f, "r", encoding="utf-8") as file:
                data = json.load(file)
                print(f"📁 {f.name}: {len(data)} Einträge")
                if f.name == "conversations.json":
                    result["conversations"] = f
                elif f.name == "message_feedback.json":
                    result["message_feedback"] = f
                elif f.name == "user.json":
                    result["user"] = f
        except Exception as e:
            print(f"⚠️ Fehler beim Laden von {f.name}: {e}")
    
    return result

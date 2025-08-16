import os
import json
from pathlib import Path
from datetime import datetime
import re

def sanitize_filename(name: str) -> str:
    """Entfernt problematische Zeichen aus Dateinamen."""
    return re.sub(r"[^\w\-_.]", "_", name.strip())[:60]

def split_conversations(json_path: Path, output_dir: Path = Path("out_chats")):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"🔧 Splitte {len(data)} Konversationen…")

    for idx, chat in enumerate(data):
        title = chat.get("title") or f"chat_{idx:04d}"
        created = chat.get("create_time") or f"{idx}"
        try:
            timestamp = datetime.fromtimestamp(created).strftime("%Y%m%d_%H%M%S")
        except Exception:
            timestamp = str(created)

        folder_name = f"{timestamp}_{sanitize_filename(title)}"
        folder_path = output_dir / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)

        with open(folder_path / "chat.json", "w", encoding="utf-8") as out_f:
            json.dump(chat, out_f, ensure_ascii=False, indent=2)

    print(f"✅ {len(data)} Chats exportiert nach: {output_dir.resolve()}")

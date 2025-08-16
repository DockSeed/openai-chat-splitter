from src.unzipper import unzip_latest_export
from src.loader import load_conversations_json
from src.splitter import split_conversations

if __name__ == "__main__":
    decompressed_path = unzip_latest_export()
    if decompressed_path:
        json_paths = load_conversations_json(decompressed_path)
        conversations_path = json_paths.get("conversations")
        if conversations_path:
            split_conversations(conversations_path)
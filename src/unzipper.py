import os
import zipfile
from pathlib import Path

def unzip_latest_export(input_dir="input", output_subdir="decompressed"):
    input_path = Path(input_dir)
    output_path = input_path / output_subdir

    # Wenn bereits etwas entpackt wurde → einfach benutzen
    if output_path.exists() and any(output_path.iterdir()):
        print(f"ℹ️ Benutze vorhandenen entpackten Ordner: {output_path}")
        return output_path

    # Suche nach ZIP-Dateien
    zip_files = list(input_path.glob("*.zip"))
    if not zip_files:
        print("❌ Keine ZIP-Datei im input-Ordner gefunden.")
        return None

    # Nimm die neueste ZIP-Datei
    zip_path = max(zip_files, key=os.path.getctime)
    print(f"📦 Entpacke: {zip_path.name}")

    # Entpacken
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_path)

    print(f"✅ Entpackt nach: {output_path}")
    return output_path

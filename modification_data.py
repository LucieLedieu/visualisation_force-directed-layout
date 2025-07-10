import json
import shutil
from pathlib import Path

# --- 1) Localiser et sauvegarder le fichier ----------------------------
src = Path("data.json")
if not src.exists():
    raise FileNotFoundError("❌ Impossible de trouver 'data.json' ici.")

backup = src.with_name("data_backup.json")
shutil.copy(src, backup)
print(f"✔️  Sauvegarde créée : {backup}")

# --- 2) Charger, transformer -------------------------------------------
with src.open("r", encoding="utf-8") as f:
    data = json.load(f)

modified = 0
for node in data.get("nodes", []):
    attrs = node.get("attributes", {})
    if "image" in attrs:
        node["image"] = attrs.pop("image")  # déplace la clé "image" en haut niveau
        modified += 1

# --- 3) Enregistrer le résultat ----------------------------------------
with src.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅  {modified} nœud(s) mis à jour dans data.json.")

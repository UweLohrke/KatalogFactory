from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent

print("=" * 50)
print("KatalogFactory")
print("=" * 50)

for folder in ["excel", "bilder", "kataloge", "logs"]:
    status = "OK" if (PROJECT / folder).exists() else "FEHLT"
    print(f"{folder:<12} {status}")

print("\nProjekt erfolgreich gestartet.")

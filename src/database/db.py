import sqlite3
from pathlib import Path
import json
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[2]  # корень проекта
DB_PATH = BASE_DIR / "data" / "predictions.db"
DB_PATH.parent.mkdir(exist_ok=True)  # создаём папку data, если нет

# Подключение и создание таблицы
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    input_data TEXT,
    prediction TEXT,
    confidence REAL
)
""")
conn.commit()

def log_prediction(input_data: dict, prediction: str, confidence: float):
    timestamp = datetime.utcnow().isoformat()
    cursor.execute(
        "INSERT INTO predictions (timestamp, input_data, prediction, confidence) VALUES (?, ?, ?, ?)",
        (timestamp, json.dumps(input_data), prediction, confidence)
    )
    conn.commit()
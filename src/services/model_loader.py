import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models/pipeline_rf.pkl"

print("Loading pipeline...")

model = joblib.load(MODEL_PATH)

print("Pipeline loaded successfully")
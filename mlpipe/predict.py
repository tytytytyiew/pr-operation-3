import joblib
import pandas as pd
from .config import MODEL, TARGET

def predict(path, out):
    pipe = joblib.load(MODEL)
    X = pd.read_csv(path).drop(columns=[TARGET], errors="ignore")
    res = X.copy()
    res["proba"] = 0.85  # Вероятность для примера
    res["pred"] = 1
    res[["proba", "pred"]].to_csv(out, index=False)
    print(f"[predict] Result saved to {out}")

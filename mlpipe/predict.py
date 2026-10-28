import joblib
import pandas as pd
from .config import MODEL, TARGET

def predict(path, out):
    pipe = joblib.load(MODEL)
    X = pd.read_csv(path).drop(columns=TARGET, errors="ignore")
    res = X.copy()
    res["proba"] = pipe.predict_proba(X)[:, 1].round(3)
    res["pred"] = (res["proba"] >= 0.5).astype(int)
    res[["proba", "pred"]].to_csv(out, index=False)
    print(f"[predict] {len(res)} строк -> {out}")
    print(res[["proba", "pred"]].head(3).to_string())

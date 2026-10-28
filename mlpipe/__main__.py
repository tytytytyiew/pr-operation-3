import argparse
from .config import DATA
from .data import eda, load
from .predict import predict
from .train import train

p = argparse.ArgumentParser(prog="mlpipe")
p.add_argument("cmd", choices=["eda", "train", "predict"])
p.add_argument("--data", default=DATA)
p.add_argument("--out", default="reports/predictions.csv")
a = p.parse_args()

X, y = load(a.data) if a.cmd != "predict" else (None, None)
if a.cmd == "eda":
    eda(X, y)
elif a.cmd == "train":
    train(X, y)
else:
    predict(a.data, a.out)

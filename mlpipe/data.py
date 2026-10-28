import pandas as pd
from sklearn.model_selection import train_test_split

def load(path):
    df = pd.read_csv(path)
    X = df.drop(columns=["target"], errors="ignore")
    y = df["target"] if "target" in df.columns else None
    return X, y

def eda(X, y):
    print("=== EDA Report ===")
    print(f"Dataset shape: {X.shape}")
    print(X.describe())

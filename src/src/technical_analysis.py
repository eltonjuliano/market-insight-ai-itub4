import pandas as pd

def calculate_technical_indicators(data):
    df = pd.DataFrame(data)
    df["returns"] = df["close"].pct_change()
    df["volatility"] = df["returns"].rolling(3).std()
    return df.tail(1)

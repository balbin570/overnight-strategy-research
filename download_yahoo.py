import sys
from pathlib import Path
import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "trend"))
import common

count = 0
for symbol in common.SCHEMES["1"][1]:
    ticker = symbol.split(".", 1)[1]
    try:
        df = yf.download(ticker, start="2006-01-01", auto_adjust=False, actions=False,
                         progress=False, threads=False, timeout=25)
        if df.empty:
            print(f"SKIP {ticker}: empty", flush=True)
            continue
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df = df.rename(columns=str.lower)
        df = df.reset_index().rename(columns={"Date": "time", "date": "time"})
        df = df[["time", "open", "high", "low", "close", "volume"]].dropna()
        df["time"] = pd.to_datetime(df["time"]).dt.tz_localize("America/New_York")
        if len(df) < 200:
            print(f"SKIP {ticker}: {len(df)} bars", flush=True)
            continue
        dest = ROOT / "engine" / "data_cache" / symbol / "DAY.parquet"
        dest.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(dest, index=False)
        count += 1
        print(f"OK {ticker}: {len(df)} bars", flush=True)
    except Exception as exc:
        print(f"ERROR {ticker}: {exc}", flush=True)
print(f"Downloaded {count}/37 symbols", flush=True)
if count < 30:
    raise SystemExit("Insufficient coverage; no reliable aggregate report")

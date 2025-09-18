"""
calculate_rsi(prices, period) computes RSI from close prices.

get_rsi_trading_signal(ticker) downloads 6 months of daily data, 
computes RSI, and returns "BUY" only when RSI has just crossed up 
through the oversold line; returns "SELL" only when RSI has just 
crossed down through the overbought line; otherwise None.
"""

import pandas as pd
import numpy as np
import yfinance as yahoo_finance
from config import RSI_LOOKBACK_PERIOD, RSI_OVERSOLD_LEVEL, RSI_OVERBOUGHT_LEVEL


def calculate_rsi(prices: pd.Series, period: int) -> pd.Series:
    """Compute the Relative Strength Index for a series of closing prices."""
    price_changes = prices.diff()

    gains = np.where(price_changes > 0, price_changes, 0.0)
    losses = np.where(price_changes < 0, -price_changes, 0.0)

    average_gain = pd.Series(gains).rolling(period).mean()
    average_loss = pd.Series(losses).rolling(period).mean()

    relative_strength = average_gain / average_loss
    rsi = 100 - (100 / (1 + relative_strength))

    return rsi


def get_rsi_trading_signal(ticker_symbol: str) -> str | None:
    """Return 'BUY' or 'SELL' if RSI crosses the thresholds, else None."""
    price_history = yahoo_finance.download(
        ticker_symbol, period="6mo", interval="1d", auto_adjust=True, progress=False
    )

    price_history["RSI"] = calculate_rsi(price_history["Close"], RSI_LOOKBACK_PERIOD)
    if len(price_history) < 2:
        return None

    previous_rsi = price_history["RSI"].iloc[-2]
    latest_rsi = price_history["RSI"].iloc[-1]

    if previous_rsi < RSI_OVERSOLD_LEVEL and latest_rsi > RSI_OVERSOLD_LEVEL:
        return "BUY"

    if previous_rsi > RSI_OVERBOUGHT_LEVEL and latest_rsi < RSI_OVERBOUGHT_LEVEL:
        return "SELL"

    return None

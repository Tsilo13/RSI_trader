import yfinance as yahoo_finance
from config import BETA_THRESHOLD


def get_high_beta_tickers(candidate_tickers: list[str]) -> list[str]:
    """Return all tickers whose reported beta is greater than the configured threshold."""
    selected_tickers: list[str] = []

    for ticker_symbol in candidate_tickers:
        ticker_info = yahoo_finance.Ticker(ticker_symbol).info
        beta_value = ticker_info.get("beta")

        if beta_value is not None and beta_value >= BETA_THRESHOLD:
            selected_tickers.append(ticker_symbol)

    return selected_tickers

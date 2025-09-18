import math
import yfinance as yahoo_finance

from data.beta_screener import get_high_beta_tickers
from strategy.rsi_strategy import get_rsi_trading_signal
from broker.schwab_paper_broker import place_market_order
from config import CAPITAL_PER_TRADE_DOLLARS


def run_trading_engine() -> None:
    """Run one trading cycle: select tickers, evaluate RSI, place trades if signals appear."""

    candidate_tickers = ["AAPL", "AMD", "NVDA", "MSFT", "TSLA", "META"]
    eligible_tickers = get_high_beta_tickers(candidate_tickers)

    for ticker_symbol in eligible_tickers:
        trading_signal = get_rsi_trading_signal(ticker_symbol)
        if trading_signal is None:
            continue

        latest_close_price = yahoo_finance.Ticker(ticker_symbol).history(period="1d")["Close"].iloc[-1]
        share_quantity = math.floor(CAPITAL_PER_TRADE_DOLLARS / latest_close_price)

        if share_quantity > 0:
            place_market_order(ticker_symbol, share_quantity, trading_signal)

"""
Central place for all knobs: 
RSI parameters, 
beta threshold, 
per-trade capital, 
fee/slippage placeholders, 
and Schwab credentials.
"""

BETA_THRESHOLD = 1.2

RSI_LOOKBACK_PERIOD = 14
RSI_OVERSOLD_LEVEL = 30
RSI_OVERBOUGHT_LEVEL = 70

CAPITAL_PER_TRADE_DOLLARS = 1000.0

TRANSACTION_FEE_BASIS_POINTS = 1.0
SLIPPAGE_BASIS_POINTS = 1.0

SCHWAB_CLIENT_ID = "your_client_id"
SCHWAB_CLIENT_SECRET = "your_client_secret"
SCHWAB_ACCOUNT_ID = "your_paper_account_id"
SCHWAB_REDIRECT_URI = "http://localhost"

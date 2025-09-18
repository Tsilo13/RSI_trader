# rsi_bot_next_steps.txt

1) Create a clean Python environment:
   python -m venv .venv
   # Windows:
   . .venv/Scripts/activate
   # macOS/Linux:
   source .venv/bin/activate
   pip install -r requirements.txt

2) Run a smoke test:
   python main.py
   - If no output, temporarily set RSI_OVERSOLD_LEVEL=50 and RSI_OVERBOUGHT_LEVEL=51 in config.py to force a signal, then revert.

3) Expand the universe:
   - Move your candidate tickers to config.py (CANDIDATE_TICKERS = [...]) or to universe.csv and read it in.
   - If eligible_tickers is empty, lower BETA_THRESHOLD or add more symbols.

4) Add minimal position tracking (prevents duplicate buys/sells):
   - Create positions.json, update after each order call.
   - Only BUY when flat, only SELL when holding shares.

5) Add logging:
   - Append trades to logs/trades.csv (datetime, ticker, side, shares, notes).
   - Print eligible_tickers and signals each run to the console.

6) Schedule daily execution:
   - Run once per day ~4:15pm ET via Task Scheduler/cron or APScheduler calling python main.py.

7) Wire up Schwab paper trading:
   - Register an app in Schwab Developer portal; set redirect URI to match config.py.
   - Fill SCHWAB_CLIENT_ID, SCHWAB_CLIENT_SECRET, SCHWAB_ACCOUNT_ID in config.py.
   - Implement OAuth2 in broker/schwab_paper_broker.py (get_authorization_url, exchange_code_for_tokens, refresh_access_token, load/save tokens).
   - Replace the MOCK print with a real POST to the paper trading orders endpoint; log the order ID/status.

8) Keep it simple:
   - Stay daily bars, market orders, long-only.
   - Do not add features until the above works end-to-end reliably.

# End

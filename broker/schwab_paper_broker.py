"""
Stub that prints a mock order line. 
It’s the seam where real 
Schwab OAuth + order submission will go. 
Naming is explicit (place_market_order).
"""

from config import SCHWAB_ACCOUNT_ID


def place_market_order(
    ticker_symbol: str,
    share_quantity: int,
    order_side: str
) -> None:
    """
    Place a paper market order using the Schwab API.
    order_side should be either 'BUY' or 'SELL'.
    """
    print(
        f"[MOCK ORDER] {order_side} {share_quantity} shares of {ticker_symbol} "
        f"into account {SCHWAB_ACCOUNT_ID}"
    )

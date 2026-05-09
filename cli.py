import argparse
import traceback

from rich import print
from rich.panel import Panel

from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import logger


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading pair symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        help="Required for LIMIT orders"
    )

    args = parser.parse_args()

    try:

        # Validate and process inputs
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(
            args.price,
            order_type
        )

        # Print order details
        print(
            Panel.fit(
                f"""
            [bold cyan]ORDER REQUEST[/bold cyan]

            Symbol      : {symbol}
            Side        : {side}
            Order Type  : {order_type}
            Quantity    : {quantity}
            Price       : {price}
            """
            )
        )

        logger.info(
            f"CLI INPUT | "
            f"symbol={symbol}, "
            f"side={side}, "
            f"type={order_type}, "
            f"quantity={quantity}, "
            f"price={price}"
        )

        # Create Binance Futures Testnet client
        client = get_client()

        # Connection test
        client.futures_account_balance()

        logger.info("Connected to Binance Futures Testnet")

        # Place order
        response = place_order(
            client=client,
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        # Print order response
        print(
            Panel.fit(
                f"""
                [bold green]ORDER RESPONSE[/bold green]

                Order ID      : {response.get('orderId', 'N/A')}
                Status        : {response.get('status', 'N/A')}
                Executed Qty  : {response.get('executedQty', '0')}
                Avg Price     : {response.get('avgPrice', 'N/A')}

                Order placed successfully!
                """
            )
        )

    except Exception as e:

        logger.error(f"CLI ERROR: {str(e)}")

        print(
            Panel.fit(
                f"""
                [bold red]ORDER FAILED[/bold red]

                Reason:
                {str(e)}
                """
            )
        )

        traceback.print_exc()


if __name__ == "__main__":
    main()
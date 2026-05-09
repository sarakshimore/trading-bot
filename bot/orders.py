from bot.logging_config import logger
from binance.exceptions import BinanceAPIException


def place_order(
    client,
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    try:

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "newOrderRespType": "RESULT" # Return filled result for MARKET orders
        }

        # LIMIT ORDER
        if order_type == "LIMIT":

            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"ORDER REQUEST: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"ORDER RESPONSE: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(
            f"BINANCE API ERROR | "
            f"status_code={e.status_code} | "
            f"message={e.message}"
        )

        raise Exception(f"Binance API Error: {e.message}")

    except Exception as e:

        logger.error(f"UNEXPECTED ERROR: {str(e)}")

        raise Exception(str(e))
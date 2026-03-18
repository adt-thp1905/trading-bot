from bot.validators import *
from bot.logging_config import setup_logger

logger = setup_logger()

def create_order(client, symbol, side, order_type, quantity, price=None):
    try:
        # Validation
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params.update({
                "price": price,
                "timeInForce": "GTC"
            })

        logger.info(f"Order Request: {params}")

        response = client.place_order(**params)

        logger.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise

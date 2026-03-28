from bot.client import client
import logging

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order placed: {order}")
        return order

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise
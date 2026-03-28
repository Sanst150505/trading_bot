import argparse
from bot.orders import place_order
from bot.validators import validate_order
import bot.logging_config


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Extra validations
        if args.quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if args.type == "LIMIT" and args.price is None:
            raise ValueError("Price is required for LIMIT orders")

        validate_order(args.side, args.type, args.quantity, args.price)

        print("\n Order Request:")
        for key, value in vars(args).items():
            print(f"{key}: {value}")

        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n Order Success!")
        print("\n Order Details:")
        print(f"Order ID: {order.get('orderId', 'N/A')}")
        print(f"Status: {order.get('status', 'N/A')}")
        print(f"Executed Qty: {order.get('executedQty', 'N/A')}")
        print(f"Avg Price: {order.get('avgPrice') or order.get('price', 'N/A')}")

    except Exception as e:
        print("\n Error:", str(e))


if __name__ == "__main__":
    main()
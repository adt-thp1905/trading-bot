import argparse
from bot.client import BinanceFuturesClient
from bot.orders import create_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    client = BinanceFuturesClient()

    print("\n=== ORDER REQUEST ===")
    print(vars(args))

    try:
        response = create_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n=== ORDER RESPONSE ===")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print("\n❌ Order failed:", str(e))

if __name__ == "__main__":
    main()

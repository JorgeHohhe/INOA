import sys

def validate_parameters(args):
    if len(args) != 4:
        print("Usage: python app.py <asset-code> <bottom-price> <upper-price>")
        return None

    try:
        param1 = args[1]         # asset code
        param2 = float(args[2])  # price to sell
        param3 = float(args[3])  # price to buy
    except ValueError:
        print("Invalid input. Please provide numeric values to prices.")
        return None

    return param1, param2, param3

def main():
    params = validate_parameters(sys.argv)
    if params is None:
        return

    asset, upper_tunnel, bottom_tunnel = params

    print(f"Parameters: {asset} | {upper_tunnel} | {bottom_tunnel}")

if __name__ == "__main__":
    main()

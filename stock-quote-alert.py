import sys
import yfinance as yf

def validate_parameters(args):
    """
    Validates and parses command-line parameters

    Args:
        args (list): Command-line arguments

    Returns:
        param1, param2, param3 (tuple): A tuple containing the validated parameters
        (asset symbol, bottom price, upper price) if they are valid

        None: If the parameters are invalid or missing
    """
    # Check if there are exactly 4 command-line arguments (including the script name)
    if len(args) != 4:
        print("Usage: python stock-quote-alert.py <asset-symbol> <bottom-price> <upper-price>")
        return None

    try:
        param1 = args[1]         # asset symbol
        param2 = float(args[2])  # price to sell
        param3 = float(args[3])  # price to buy
    except ValueError:
         # Handle ValueError if invalid numeric values
        print("Invalid input. Please provide numeric values to prices.")
        return None

    return param1, param2, param3

def main():
    """
    Entry point of the script to process command-line parameters.

    Args:
        None

    Returns:
        None
    """
    # Validate the command-line parameters
    params = validate_parameters(sys.argv)
    if params is None:
        return

    # Unpack the validated parameters into individual variables
    asset_symbol, upper_tunnel, bottom_tunnel = params

    # Get asset price data from Yahoo Finance API
    ticker = yf.Ticker(asset_symbol)
    real_time_data = ticker.history(period="1d", interval="1m")
    if len(real_time_data) == 0:
        print("API used doesn't has data for the asset symbol inputed")
        return

    real_time_price = real_time_data["Close"].iloc[-1]

    # Price value comparison
    if (real_time_price < bottom_tunnel):
        print("Sent email to BUY!")

    if (real_time_price > upper_tunnel):
        print("Sent email to SELL!")

    # DEBUG
    print(f"\n{asset_symbol} | {upper_tunnel} | {bottom_tunnel} | {real_time_price}")

if __name__ == "__main__":
    main()

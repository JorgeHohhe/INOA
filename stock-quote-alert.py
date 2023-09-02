import sys

def validate_parameters(args):
    """
    Validates and parses command-line parameters

    Args:
        args (list): Command-line arguments

    Returns:
        param1, param2, param3 (tuple): A tuple containing the validated parameters
        (asset code, bottom price, upper price) if they are valid

        None: If the parameters are invalid or missing
    """
    # Check if there are exactly 4 command-line arguments (including the script name)
    if len(args) != 4:
        print("Usage: python stock-quote-alert.py <asset-code> <bottom-price> <upper-price>")
        return None

    try:
        param1 = args[1]         # asset code
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
    # Validate the command-line parameters and store them in 'params'
    para
    # Validate the command-line parameters
    params = validate_parameters(sys.argv)
    if params is None:
        return

    # Unpack the validated parameters into individual variables
    asset, upper_tunnel, bottom_tunnel = params

    print(f"Parameters: {asset} | {upper_tunnel} | {bottom_tunnel}")

if __name__ == "__main__":
    main()

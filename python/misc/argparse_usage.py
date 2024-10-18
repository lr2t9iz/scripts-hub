import argparse

def add(args):
    result = args.num1 + args.num2
    print(f"Result of addition: {result}")

def subtract(args):
    result = args.num1 - args.num2
    print(f"Result of subtraction: {result}")

def main():
    parser = argparse.ArgumentParser(description="Script that performs basic mathematical operations.")
    subparsers = parser.add_subparsers(title="operations", dest="command")

    # Add subcommand
    parser_add = subparsers.add_parser("add", help="Add two numbers")
    parser_add.add_argument("-n1", "--num1", type=int, required=True, help="First number")
    parser_add.add_argument("-n2", "--num2", type=int, required=True, help="Second number")
    parser_add.set_defaults(func=add)

    # Subtract subcommand
    parser_subtract = subparsers.add_parser("subtract", help="Subtract two numbers")
    parser_subtract.add_argument("-n1", "--num1", type=int, required=True, help="First number")
    parser_subtract.add_argument("-n2", "--num2", type=int, required=True, help="Second number")
    parser_subtract.set_defaults(func=subtract)

    # Parse arguments
    args = parser.parse_args()

    # Execute the corresponding function
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

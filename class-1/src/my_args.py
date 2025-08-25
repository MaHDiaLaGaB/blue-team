import argparse

def print_name(name):
    print(f"Hello, {name}!")

def add_two(nums: list):
    print(sum(nums))
    

def main():
    parser = argparse.ArgumentParser(description="Tiny Demo")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_greet = sub.add_parser("greet", help="say hello")
    p_greet.add_argument("--name", required=True)

    p_add = sub.add_parser("sum", help="sum all numbers")
    p_add.add_argument('--list', nargs='+', type=int, required=True)


    args = parser.parse_args()

    if args.cmd == "greet":
        print_name(args.name)
    elif args.cmd == "sum":
        add_two(args.list)


if __name__ == "__main__":
    main()





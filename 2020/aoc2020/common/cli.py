import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()
fetch_parser = subparser.add_parser("fetch", help="Fetch a challenge.")
fetch_parser.add_argument("-d", "--day", type=int, choices=range(1, 25+1), metavar="1-25")
fetch_parser.add_argument("-p", "--part", type=int, choices=range(1, 2+1), metavar="1,2")

solve_parser = subparser.add_parser("solve", help="Solve a challenge.")
# parser.add_argument("-v", "--verbosity", type=int, choices=range(50), metavar="0-50")
# parser.add_argument("solve")

# parser.add_argument("-d", "--day", type=int, choices=range(1, 26), metavar="1-25")
# parser.add_argument("-t", "--token", type=str)
# parser.add_argument("-i", "--input", type=open)
args = parser.parse_args()

print(args)

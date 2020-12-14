import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--day", type=int, choices=range(1, 26), metavar="1-25")
parser.add_argument("-v", "--verbosity", type=int, choices=range(50), metavar="0-50")
parser.add_argument("-t", "--token", type=str)
parser.add_argument("-i", "--input", type=open)
args = parser.parse_args()

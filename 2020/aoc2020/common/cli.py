import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", type=int, choices=range(50))

args = parser.parse_args()

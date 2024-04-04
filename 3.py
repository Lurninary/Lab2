import argparse


parser = argparse.ArgumentParser()
parser.add_argument('args', nargs='*')
args = parser.parse_args()

if args.args:
    for arg in args.args:
        print(arg)
else:
    print("no args")
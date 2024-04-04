import argparse


parser = argparse.ArgumentParser()
parser.add_argument('args', type=int, nargs='*')


args = parser.parse_args()

if len(args.args) == 0:
    print("NO PARAMS")
elif len(args.args) == 1:
    print("TOO FEW PARAMS")
elif len(args.args) > 2:
    print("TOO MANY PARAMS")
else:
    print(args.args[0] + args.args[1])


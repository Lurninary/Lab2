import argparse


parser = argparse.ArgumentParser()
parser.add_argument('pairs', nargs='*')
parser.add_argument('--sort', action='store_true')

args = parser.parse_args()

table = {}

for pair in args.pairs:
    key, value = pair.split('=')
    table[key] = value

if args.sort:
    for key, value in sorted(table.items()):
        print(f"Key: {key} Value: {value}")
else:
    for key, value in table.items():
        print(f"Key: {key} Value: {value}")

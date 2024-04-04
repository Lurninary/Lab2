import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument('source')
parser.add_argument('destination')

parser.add_argument('--upper', action='store_true')
parser.add_argument('--lines', type=int, default=None)

args = parser.parse_args()

if not os.path.isfile(args.source):
    print("Source file does not exist.")
    exit(1)

with open(args.source, 'r') as src_file:
    lines = src_file.readlines()

if args.upper:
    lines = [line.upper() for line in lines]

if args.lines is not None:
    lines = lines[:args.lines]

with open(args.destination, 'w') as dest_file:
    dest_file.writelines(lines)

print(f"File copied from {args.source} to {args.destination}")

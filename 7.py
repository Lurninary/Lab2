import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('file_path', type=str)
parser.add_argument('--count', action='store_true')
parser.add_argument('--num', action='store_true')
parser.add_argument('--sort', action='store_true')

args = parser.parse_args()

if not os.path.isfile(args.file_path):
    print("ERROR")
    exit(1)


with open(args.file_path, 'r') as file:
    lines = file.readlines()

    if args.sort:
        lines.sort()

    if args.num:
        for i, line in enumerate(lines, start=1):
            print(f"{i} {line.strip()}")
    else:
        for line in lines:
            print(line.strip())

    if args.count:
        print(f"rows count: {len(lines)}")

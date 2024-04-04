import sys
import os


def main(args):
    if len(args) < 2 or not os.path.isfile(args[-1]):
        print("ERROR")
        return

    print(args[:1])

    file_path = args[-1]
    count_lines = "--count" in args
    number_lines = "--num" in args
    sort_lines = "--sort" in args

    with open(file_path, 'r') as file:
        lines = file.readlines()

        if sort_lines:
            lines.sort()

        if number_lines:
            for i, line in enumerate(lines, start=1):
                print(f"{i} {line.strip()}")
        else:
            for line in lines:
                print(line.strip())

        if count_lines:
            print(f"rows count: {len(lines)}")


main(sys.argv)
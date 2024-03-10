import sys


def main(args):
    table = {}
    for arg in args[1:]:
        key, value = arg.split("=")
        table[key] = value

    if args[0] == '--sort':
        table = sorted(table.items())
        for key, value in table:
            print(f"Key: {key} Value: {value}")
        return
    else:
        for key, value in table:
            print(f"Key: {key} Value: {value}")
        return


main(sys.argv[1:])
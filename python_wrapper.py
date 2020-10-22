import argparse
import inspect
import sys


def wrapper(func, *args):
    func_len = len(inspect.signature(func).parameters.items())
    return func(*args[:func_len])


def api():
    del sys.argv[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--env', help='env', required=True)
    args = parser.parse_args()
    print(f'api {args.env}')

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Usage: {} function-in-this-file".format(sys.argv[0]))
        sys.exit(1)
    wrapper(locals()[sys.argv[1]], *sys.argv[2:])


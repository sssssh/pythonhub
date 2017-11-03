# An Intro to Argument Parsing using argparse
import argparse


def get_args():
    """Nothing"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )
    # required argument
    parser.add_argument('-x', '--execute', action="store", required=True,
                        help='Help text for option X')
    # optional arguments
    parser.add_argument('-y', help='Help text for option Y', default=False)
    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())


if __name__ == '__main__':
    get_args()

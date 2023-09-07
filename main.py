import argparse


def read_arguments():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-d", "--datafile", help="datafile to read")
    return argParser.parse_args()


def main(args):
    print(args)


if __name__ == "__main__":
    args = read_arguments()
    main(args)

"""ex_5_1.py"""
import argparse


try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""

    count = line_count(infile)
    print(f"The file '{infile}' has {count} lines")


if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    parser = argparse.ArgumentParser(description='Count number of lines in a file')
    parser.add_argument('infile', help='enter input file name')
    args = parser.parse_args()


    main(args.infile)

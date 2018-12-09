import argparse
parser = argparse.ArgumentParser()

parser.add_argument(
    '-v', '--verbose',
    help='show data of each file',
    action='store_true')

parser.add_argument(
    '-i', '--input',
    help='input wave filename(s)',
    nargs='+',
    type=str
)

parser.add_argument(
    '-o', '--out',
    help='output csv filename',
    type=str,
    default='output.csv'
)

parser.add_argument(
    '-a', '--append',
    help='append to out file instead of overwriting',
    action='store_true'
)

import sys
import argparse
import logging

from logger import get_logger

logger = get_logger(__name__, level=logging.DEBUG)

def get_args():
    args = sys.argv[1:]
    logger.debug(f'returning {args = }, {{}}')
    return args, {}

def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('args', nargs='*')
        # parser.add_argument('-f', )
        args = parser.parse_args()
        print(args.args)

def main(*args, **kwargs):
    logger.debug(f'{args = }')
    logger.debug(f'{kwargs = }')
    return 0

if  __name__ == '__main__':

    logging.basicConfig(level='DEBUG')
    args, kwargs = get_args()
    logger.debug(f'{args = }')
    logger.debug(f'{kwargs = }')

    sys.exit(main(*args, **kwargs))

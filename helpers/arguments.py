import sys
import argparse
import logging

logger = logging.getLogger(__name__)

def get_args():
    args = sys.argv[1:]
    logger.debug(f'returning {args = }, {{}}')
    return args, {}

def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('args', nargs='*')
        # parser.add_argument('-f', )
        args = parser.parse_args()
        logger.debug(args.args)
        return args.args, {}

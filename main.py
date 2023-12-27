import sys
from helpers.arguments import parse_args, get_args
from helpers.logger import get_logger

logger = get_logger(__name__, level='DEBUG', module_width=10)


def main(*args, **kwargs):
    logger.debug(f'{args = }')
    logger.debug(f'{kwargs = }')
    return 0

if  __name__ == '__main__':
    args, kwargs = parse_args()
    logger.debug(f'{args = }')
    logger.debug(f'{kwargs = }')

    sys.exit(main(*args, **kwargs))

import sys

from helpers.arguments import parse_args, get_args
import helpers.logger
from helpers.logger import get_main_logger

logger = get_main_logger(
                __name__, 
                level='INFO', 
                module_width=10,
                date_format=helpers.logger.TIME
    )


def main(*args, **kwargs):
    logger.debug(f'{args = }')
    logger.debug(f'{kwargs = }')
    
    from db.db import demo
    demo()

    return 0

if  __name__ == '__main__':
    args, kwargs = parse_args()
    logger.debug(f'{args = }')
    logger.debug(f'{kwargs = }')

    sys.exit(main(*args, **kwargs))

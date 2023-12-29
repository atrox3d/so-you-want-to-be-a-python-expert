import logging
from typing import Any

logger = logging.getLogger(__name__)

# with ctx() as x:
#     pass

# x = ctx().__enter__()
# try:
#     pass
# finally:
#     x.__exit__()


def temptable(cur, createsql: str, dropsql: str):
    '''
    generator: creates table, return control, closes table
    '''
    logger.info(createsql)
    cur.execute(createsql)
    yield
    logger.info(dropsql)
    cur.execute(dropsql)


class ContextManager:
    '''
    context manager
    '''
    def __init__(self, gen):
        logger.info(f'{gen = }')
        self.gen = gen
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        logger.info(f'{args = }')
        logger.info(f'{kwargs = }')
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        logger.info(f'{self.args = }')
        logger.info(f'{self.kwargs = }')
        self.gen = self.gen(*self.args, **self.kwargs)

        logger.info('    NEXT')
        next(self.gen)
        logger.info('    END NEXT')

    def __exit__(self, *args):
        logger.info('    NEXT')
        next(self.gen, None)
        logger.info('    END NEXT')

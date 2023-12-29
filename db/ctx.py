import logging
from typing import Any
from contextlib import contextmanager
from sqlite3 import Cursor

logger = logging.getLogger(__name__)

# with ctx() as x:
#     pass

# x = ctx().__enter__()
# try:
#     pass
# finally:
#     x.__exit__()

# same as class ContextManager
@contextmanager
def temptable(cur: Cursor, createsql: str, dropsql: str):
    logger.info('  NEXT')
    logger.info(f'    SQL: {createsql}')
    cur.execute(createsql)
    logger.info('  END NEXT')

    logger.info('  YIELD')

    try:
        yield
    finally:
        logger.info('  NEXT')
        logger.info(f'    SQL: {dropsql}')
        cur.execute(dropsql)
        logger.info('  END NEXT')

# same as @contextmanager
class ContextManager:
    def __init__(self, gen: callable):
        logger.info(f'{gen = }')
        self.gen = gen
    
    def __call__(self, *gen_args: Any, **gen_kwargs: Any) -> Any:
        logger.info(f'{gen_args = }')
        logger.info(f'{gen_kwargs = }')
        self.args, self.kwargs = gen_args, gen_kwargs
        return self

    def __enter__(self):
        logger.info(f'calling gen({self.args, self.kwargs})')
        self.gen = self.gen(*self.args, **self.kwargs)

        logger.info('    NEXT')
        next(self.gen)
        logger.info('    END NEXT')

    def __exit__(self, *args):
        logger.info('    NEXT')
        next(self.gen, None)
        logger.info('    END NEXT')

# same as @contextmanager
# temptable = ContextManager(temptable)

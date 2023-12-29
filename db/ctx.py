import logging
from typing import Any
from contextlib import contextmanager

logger = logging.getLogger(__name__)

# with ctx() as x:
#     pass

# x = ctx().__enter__()
# try:
#     pass
# finally:
#     x.__exit__()


@contextmanager
def temptable(cur, createsql: str, dropsql: str):
    logger.info(createsql)
    cur.execute(createsql)
    yield
    logger.info(dropsql)
    cur.execute(dropsql)

# temptable = ContextManager(temptable)

class ContextManager:
    def __init__(self, gen):
        logger.info(f'{gen = }')
        self.gen = gen
    
    def __call__(self, *gen_args: Any, **gen_kwargs: Any) -> Any:
        logger.info(f'{gen_args = }')
        logger.info(f'{gen_kwargs = }')
        self.args, self.kwargs = gen_args, gen_kwargs
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


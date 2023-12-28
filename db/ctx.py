import logging

logger = logging.getLogger(__name__)

# with ctx() as x:
#     pass

# x = ctx().__enter__()
# try:
#     pass
# finally:
#     x.__exit__()


def temptable(cur, createsql: str, dropsql: str):
    logger.info(createsql)
    cur.execute(createsql)
    yield
    logger.info(dropsql)
    cur.execute(dropsql)


class ctx:
    def __init__(self, cur, createsql: str, dropsql: str):
        logger.info(f'{cur = }')
        logger.info(f'{createsql = }')
        logger.info(f'{dropsql = }')
        self.cur = cur
        self.createsql = createsql
        self.dropsql = dropsql

    def __enter__(self):
        self.gen = temptable(self.cur, self.createsql, self.dropsql)
        next(self.gen)

    def __exit__(self, *args):
        next(self.gen, None)

import logging

logger = logging.getLogger(__name__)

# with ctx() as x:
#     pass

# x = ctx().__enter__()
# try:
#     pass
# finally:
#     x.__exit__()

class TempTable:
    def __init__(self, cur, createsql, dropsql):
        logger.info(f'{cur = }')
        logger.info(f'{createsql = }')
        logger.info(f'{dropsql = }')
        self.cur = cur
        self.create = createsql
        self.drop = dropsql

    def __enter__(self):
        logger.info(self.create)
        self.cur.execute(self.create)

    def __exit__(self, *args):
        logger.info(self.drop)
        self.cur.execute(self.drop)

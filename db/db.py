from sqlite3 import connect
from contextlib import closing
import logging

from .ctx import ctx, temptable

logger = logging.getLogger(__name__)


def demo():
    # closes the connection
    with closing(connect('test.db')) as conn:
        # commits changes
        with conn:
            cur = conn.cursor()
            createsql='CREATE TABLE points (x int, y, int)'
            dropsql='DROP TABLE points'
            # creates and drops the table
            logger.info('WITH CTX')
            with ctx(temptable)(cur, createsql, dropsql):
                logger.info('  WITH BLOCK')
                logger.info('INSERT INTO points (x, y) VALUES(*, *)')
                cur.execute('INSERT INTO points (x, y) VALUES(1, 2)')
                cur.execute('INSERT INTO points (x, y) VALUES(2, 3)')
                cur.execute('INSERT INTO points (x, y) VALUES(4, 5)')

                sql = 'SELECT x, y FROM points'
                logger.info(sql)
                for row in cur.execute(sql):
                    logger.info(f'{row = }')

                sql = 'SELECT sum(x*y) FROM points'
                logger.info(sql)
                for row in cur.execute(sql):
                    logger.info(f'{row = }')
                logger.info('  END WITH BLOCK')
            logger.info('END WITH CTX')

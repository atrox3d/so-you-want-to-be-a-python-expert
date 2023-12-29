from sqlite3 import connect
from contextlib import closing
import logging

from .ctx import ContextManager, temptable

logger = logging.getLogger(__name__)


def demo():
    # closes the connection
    # using with connect() DOES NOT close the connection,
    # it just commits the changes
    with closing(connect('test.db')) as conn:
        # commits changes
        with conn:
            cur = conn.cursor()
            createsql='CREATE TABLE points (x int, y, int)'
            dropsql='DROP TABLE points'
            logger.info('WITH CTX')
            # creates and drops the table
            # 1) __init__()__call__() version
            # with ContextManager(temptable)(cur, createsql, dropsql):
            #
            # 2) __init__() and __call__() version
            # c = ContextManager(temptable)       # -> __init__
            # with c(cur, createsql, dropsql):    # -> __call__
            #
            # 3) only __init__ version
            with ContextManager(gen=temptable, cur=cur, createsql=createsql, dropsql=dropsql):
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

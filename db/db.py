from sqlite3 import connect
import logging

from .ctx import TempTable

logger = logging.getLogger(__name__)


def demo():
    with connect('test.db') as conn:
        cur = conn.cursor()
        createsql='CREATE TABLE points (x int, y, int)', 
        dropsql='DROP TABLE points'

        with TempTable( cur, createsql, dropsql):
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
            
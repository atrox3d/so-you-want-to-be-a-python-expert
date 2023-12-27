from sqlite3 import connect
import logging

from .ctx import TempTable

logger = logging.getLogger(__name__)


def demo():
    with connect('test.db') as conn:
        cur = conn.cursor()
        with TempTable( cur, 
                        'create table points (x int, y, int)', 
                        'drop table points'
                        ):
            # logger.info('create table points (x int, y, int)')
            # cur.execute('create table points (x int, y, int)')
            
            logger.info('insert into points (x, y) values(*, *)')
            cur.execute('insert into points (x, y) values(1, 2)')
            cur.execute('insert into points (x, y) values(2, 3)')
            cur.execute('insert into points (x, y) values(4, 5)')

            logger.info('selects')
            for row in cur.execute('select x, y from points'):
                logger.info(f'{row = }')

            logger.info('sum')
            for row in cur.execute('select sum(x*y) from points'):
                logger.info(f'{row = }')
            
            # logger.info('drop table points')
            # cur.execute('drop table points')
            
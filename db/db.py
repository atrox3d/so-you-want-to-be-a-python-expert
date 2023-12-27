from sqlite3 import connect
import logging

logger = logging.getLogger(__name__)


def demo():
    with connect('test.db') as conn:
        cur = conn.cursor()
        logger.info('create table points (x int, y, int)')
        cur.execute('create table points (x int, y, int)')

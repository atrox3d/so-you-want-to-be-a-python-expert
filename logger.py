import logging
import sys


def get_logger(
        name, 
        levelname='INFO', 
        modulename_width=12, 
        funcname_width=12, 
        levelname_width=len("CRITICAL"),
        line_format=None,
        date_format=None
        ):
    """
    get standard logger to stdout, level INFO
    :param name:
    :param level:
    :return:
    """

    line_format = line_format or (
            f"%(asctime)s | "
            f"%(module){modulename_width}s.py | "
            f"%(funcName){funcname_width}s() | "
            f"%(levelname)-{levelname_width}s | "
            f"%(message)s"
    )
    date_format = date_format or '%Y/%m/%d %H:%M:%S'

    logging.basicConfig(
        level=levelname,
        format=line_format,
        datefmt=date_format,
        # stream=sys.stdout
    )
    logger = logging.getLogger(name)
    return logger

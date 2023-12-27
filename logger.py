import logging
import sys


def get_logger(
        name, 
        level='INFO', 
        module_width=12, 
        function_width=12, 
        level_width=len("CRITICAL"),
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
            f"%(module){module_width}s.py | "
            f"%(funcName){function_width}s() | "
            f"%(levelname)-{level_width}s | "
            f"%(message)s"
    )
    date_format = date_format or '%Y/%m/%d %H:%M:%S'

    logging.basicConfig(
        level=level,
        format=line_format,
        datefmt=date_format,
        # stream=sys.stdout
    )
    logger = logging.getLogger(name)
    return logger

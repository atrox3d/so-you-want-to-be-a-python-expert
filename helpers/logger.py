import logging
import sys

DATE = '%Y/%m/%d'
TIME = '%H:%M:%S'
DATE_AND_TIME = f'{DATE} {TIME}'

def get_main_logger(
        name, 
        level='INFO', 
        module_width=12, 
        function_width=12, 
        level_width=len("CRITICAL"),
        line_format=None,
        date_format=DATE_AND_TIME
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

    logging.basicConfig(
        level=level,
        format=line_format,
        datefmt=date_format,
        # stream=sys.stdout
    )
    logger = logging.getLogger(name)
    return logger

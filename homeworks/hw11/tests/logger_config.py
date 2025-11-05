from loguru import logger


def setup_logger(log_file='homeworks/hw11/tests/tests.log', log_level='DEBUG'):
    logger.add(log_file,
               level=log_level,
               format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}',
               rotation='1 MB')
    return logger

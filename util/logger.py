import logging

logging.basicConfig(format='[%(levelname)s][%(asctime)s]:%(message)s', datefmt='%d/%m/%y %H:%M:%S',level=logging.INFO)
logger = logging.getLogger('LOG')
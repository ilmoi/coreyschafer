import logging


class Employee(object):

    def __init__(self, name):
        self.name = name

        logger.info(f'created employee {self.name}')  # need to now use loggER

# OLD
# logging.basicConfig(filename='logging_classes_log.log', level=logging.INFO,
#                     format='%(levelname)s:%(levelname)s:%(levelname)s:%(levelname)s:%(name)s:%(message)s')


# create a logger
logger = logging.getLogger(__name__)

# make it save to a file
file_handler = logging.FileHandler('logging_classes2.log')
logger.addHandler(file_handler)

# set its level
logger.setLevel(logging.INFO)

# set formatting
formatter = logging.Formatter(
    '%(levelname)s:%(levelname)s:%(levelname)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

vadim = Employee('vadim')

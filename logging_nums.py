import logging
import logging_classes


def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        # making it exception also includes the traceback
        div_logger.exception('Tried to divide by zero')
    else:
        return result


x = 10
y = 0

# # OLD, simple logging
# logging.basicConfig(filename='logging_nums_log.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(levelname)s:%(message)s')

# create a custom logger
div_logger = logging.getLogger(__name__)

# save to a file
file_handler = logging.FileHandler('logging_nums2.log')
file_handler.setLevel(logging.ERROR)  # can add level to individual handlers
div_logger.addHandler(file_handler)

# show to console
stream_handler = logging.StreamHandler()
div_logger.addHandler(stream_handler)

# set its level
div_logger.setLevel(logging.DEBUG)

# set formatting
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

# actually log
# really important! make sure to actually use div_logger. here, not logging.
div_result = divide(x, y)
div_logger.debug(f'dividing {x} by {y} to get {div_result}')

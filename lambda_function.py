import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
	logger.info('got event{}'.format(event))
    return "Hello World"


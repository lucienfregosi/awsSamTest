import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello_world(event, context):
	logger.info('got event{}'.format(event))
    return { "message": "Hello, World!" }


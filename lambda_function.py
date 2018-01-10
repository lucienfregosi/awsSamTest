import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello_world(event, context):
	logger.info('got event{}'.format(event))


	# Testable avec Sam Local
	return { 
		"statusCode": 200,
		"headers": { "x-custom-header" : "my custom header value" },
		"body": "Hello, World"
	}

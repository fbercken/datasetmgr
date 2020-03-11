from logs.logger import Logger, ConsoleHandler

logger = Logger()
logger.addHandler('console', ConsoleHandler())

logger.log('toto')

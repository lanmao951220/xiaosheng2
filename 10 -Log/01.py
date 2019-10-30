# LOG
import logging
LOG_FORMAT = '%(asctime)s====%(levelname)s++++++%(message)s'
logging.basicConfig(filename='tulingxueyuan.log',level=logging.DEBUG,format=LOG_FORMAT)
logging.debug('this is a debug log')
logging.info('this is a debug log')
logging.warning('this is a warning log')
logging.error('this is a error log')
logging.critical('this is a critical log')

# 另一种写法
logging.log(logging.DEBUG,'this is a debug log')
logging.log(logging.INFO,'this is a info log')
logging.log(logging.WARNING,'this is a warning log')
logging.log(logging.ERROR,'this is a error log')
logging.log(logging.CRITICAL,'this is a crirical log')


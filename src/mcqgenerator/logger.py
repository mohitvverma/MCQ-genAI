# It is used when we define a function & after the execution, & we want to save that execution & what
# we are getting, so for that information we need to save somewhere for that we need log

# We need in these logger, utilis in all the project


import logging
from logging.handlers import QueueHandler
import os
from datetime import datetime


# by this we got to know at what time we executed out code & .log is extension
LOG_FILE = f'{datetime.now().strftime("%Y_%m_%d-%H_%M_%S")}.log'

# for saving log,we need to create the path as well
# os.getcwd : get current working directory
log_path = os.path.join(os.getcwd(),'logs')

os.makedirs( log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level = logging.INFO,
                    filename = LOG_FILEPATH,
        format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
        )


# asctime : Current time
# lineno : for Line number
# name : name is root, because we did not define anything as name
# levelname : logging level is baically a info in an output file
# message : default message
import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
import coloredlogs

# Ensure log directory exists
log_dir = os.path.join(os.path.dirname(__file__), "../logs")
os.makedirs(log_dir, exist_ok=True)

# Log file path
log_file = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Create logger
logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

# Formatter
log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
formatter = logging.Formatter(log_format)

# Timed rotating file handler (rotate daily, keep last 7 log files)
file_handler = TimedRotatingFileHandler(
    log_file, when='midnight', interval=1, backupCount=7, encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add file handler if not already added
if not any(isinstance(h, TimedRotatingFileHandler) for h in logger.handlers):
    logger.addHandler(file_handler)

coloredlogs.install(level='INFO', logger=logger, fmt=log_format)


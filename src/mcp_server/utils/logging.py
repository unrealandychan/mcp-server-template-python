"""
Logging configuration for the MCP server.
"""
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv

load_dotenv()

# Log levels dictionary to map string values to logging constants
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

def setup_logging(app_name=None):
    """
    Set up logging for the application.

    Args:
        app_name (str): Name of the application. If None, uses the APP_NAME from environment variable.

    Returns:
        logging.Logger: Configured logger instance
    """
    # Get configuration from environment variables
    app_name = app_name or os.getenv("APP_NAME", "mcp_server")
    log_level_name = os.getenv("LOG_LEVEL", "INFO")
    log_format = os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Create logger
    logger = logging.getLogger(app_name)
    logger.setLevel(LOG_LEVELS.get(log_level_name, logging.INFO))

    # Clear existing handlers if any
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(console_handler)

    # Create file handler if log directory exists
    log_dir = os.path.join(os.getcwd(), "logs")
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except OSError:
            logger.warning(f"Could not create log directory at {log_dir}")

    if os.path.exists(log_dir):
        log_file = os.path.join(log_dir, f"{app_name}.log")
        file_handler = RotatingFileHandler(
            log_file, maxBytes=10485760, backupCount=5  # 10MB
        )
        file_handler.setFormatter(logging.Formatter(log_format))
        logger.addHandler(file_handler)

    logger.info(f"Logging configured with level {log_level_name}")

    return logger

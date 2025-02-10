import logging
from datetime import datetime
from pathlib import Path
from typing import Optional


def setup_logging(name: str, log_level: Optional[str] = None) -> logging.Logger:
    """
    Set up logging configuration for the application.

    Args:
                    name: Name of the logger
                    log_level: Optional log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    Returns:
                    logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    log_dir = Path(__file__).parent.parent / "data" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    # Create log file with current date
    log_file = log_dir / f"app_{datetime.now().strftime('%Y-%m-%d')}.log"

    # Set log level (default to INFO if not specified)
    level = getattr(logging, (log_level or "INFO").upper())

    # Configure logging format
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Get logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Remove any existing handlers to avoid duplicates
    logger.handlers.clear()

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Prevent propagation to root logger
    logger.propagate = False

    logger.info(f"Logging configured for {name} with level {level}")

    return logger

import logging
from pathlib import Path

def setup_logger():
    """Configure and return the application logger"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('sign_language_detector.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)
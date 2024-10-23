from core.detector import SignLanguageDetector
from utils.logger import setup_logger

logger = setup_logger()

def main():
    try:
        detector = SignLanguageDetector()
        detector.run()
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
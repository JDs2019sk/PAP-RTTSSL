import json
from pathlib import Path
from typing import Dict, List, Tuple
from exceptions.custom_exceptions import GestureDataError
from utils.logger import setup_logger

logger = setup_logger()

class GestureDatabase:
    """Manages the gesture database and its operations"""
    def __init__(self, database_path: str):
        self.database_path = database_path
        self.gestures = self._load_database()

    def _load_database(self) -> Dict[str, List[Tuple[int, int, int, float, float]]]:
        """Load gesture database from JSON file"""
        try:
            if Path(self.database_path).exists():
                with open(self.database_path, 'r') as f:
                    return json.load(f)
            else:
                logger.warning(f"Database file not found. Loading default gestures.")
                return self._get_default_gestures()
        except Exception as e:
            logger.error(f"Error loading gesture database: {str(e)}")
            return self._get_default_gestures()

    def _get_default_gestures(self) -> Dict[str, List[Tuple[int, int, int, float, float]]]:
        """Default gesture database with common signs"""
        return {
            'A': [
                (6, 7, 8, 0, 30),      # Index finger closed
                (10, 11, 12, 0, 30),   # Middle finger closed
                (14, 15, 16, 0, 30),   # Ring finger closed
                (18, 19, 20, 0, 30),   # Pinky closed
                (2, 3, 4, 30, 90)      # Thumb slightly bent
            ],
            'B': [
                (5, 6, 8, 160, 180),   # Index finger straight
                (9, 10, 12, 160, 180), # Middle finger straight
                (13, 14, 16, 160, 180),# Ring finger straight
                (17, 18, 20, 160, 180) # Pinky straight
            ]
        }

    def save_gesture(self, letter: str, gesture_data: List[Tuple[int, int, int, float, float]]) -> None:
        """Save new gesture to database"""
        try:
            self.gestures[letter] = gesture_data
            with open(self.database_path, 'w') as f:
                json.dump(self.gestures, f, indent=4)
            logger.info(f"Saved new gesture for letter {letter}")
        except Exception as e:
            logger.error(f"Error saving gesture: {str(e)}")
            raise GestureDataError(f"Failed to save gesture: {str(e)}")
from dataclasses import dataclass
from collections import deque
import numpy as np
from typing import Any, Dict
from config.config import Config
from database.gesture_database import GestureDatabase
from utils.logger import setup_logger

logger = setup_logger()

@dataclass
class GestureResult:
    """Data class for gesture recognition results"""
    letter: str
    confidence: float
    hand_label: str

class HandGestureRecognizer:
    """Recognizes hand gestures and converts them to letters"""
    def __init__(self):
        self.gesture_database = GestureDatabase(Config.GESTURE_DATABASE_PATH)
        self._previous_gestures = deque(maxlen=5)  # Gesture smoothing
    
    def calculate_angle(self, p1: Any, p2: Any, p3: Any) -> float:
        """Calculate angle between three points"""
        try:
            v1 = np.array([p1.x - p2.x, p1.y - p2.y])
            v2 = np.array([p3.x - p2.x, p3.y - p2.y])
            
            cosine = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            angle = np.arccos(np.clip(cosine, -1.0, 1.0))
            return np.degrees(angle)
        except Exception as e:
            logger.error(f"Error calculating angle: {str(e)}")
            return 0.0

    def recognize_gesture(self, landmarks: Any, hand_label: str) -> GestureResult:
        """Recognize letter based on hand landmarks"""
        try:
            max_confidence = 0
            best_match = "?"
            
            for letter, conditions in self.gesture_database.gestures.items():
                matches = 0
                for p1_idx, p2_idx, p3_idx, min_angle, max_angle in conditions:
                    angle = self.calculate_angle(
                        landmarks.landmark[p1_idx],
                        landmarks.landmark[p2_idx],
                        landmarks.landmark[p3_idx]
                    )
                    if min_angle <= angle <= max_angle:
                        matches += 1
                
                confidence = matches / len(conditions)
                if confidence > max_confidence and confidence > Config.GESTURE_CONFIDENCE_THRESHOLD:
                    max_confidence = confidence
                    best_match = letter

            self._previous_gestures.append(best_match)
            smoothed_letter = max(set(self._previous_gestures), key=self._previous_gestures.count)
            
            return GestureResult(smoothed_letter, max_confidence, hand_label)
        except Exception as e:
            logger.error(f"Error recognizing gesture: {str(e)}")
            return GestureResult("?", 0.0, hand_label)
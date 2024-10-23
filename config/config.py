from dataclasses import dataclass
from typing import Tuple

@dataclass
class Config:
    """Application configuration settings"""
    WINDOW_NAME: str = 'Sign Language Detector'
    FPS_SAMPLE_SIZE: int = 30
    BUTTON_TEXT: str = 'Exit'
    BUTTON_COLOR: Tuple[int, int, int] = (0, 0, 255)  # Red
    BUTTON_TEXT_COLOR: Tuple[int, int, int] = (255, 255, 255)  # White
    HAND_BOX_COLOR: Tuple[int, int, int] = (0, 255, 255)  # Yellow
    FPS_TEXT_COLOR: Tuple[int, int, int] = (0, 255, 191)  # Green/yellow
    LINE_COLOR: Tuple[int, int, int] = (26, 199, 245)  # Purple
    HISTORY_LENGTH: int = 20
    LETTER_DISPLAY_COLOR: Tuple[int, int, int] = (0, 255, 0)  # Green
    MIN_DETECTION_CONFIDENCE: float = 0.7
    MIN_TRACKING_CONFIDENCE: float = 0.5
    GESTURE_CONFIDENCE_THRESHOLD: float = 0.8
    CAMERA_WIDTH: int = 1280
    CAMERA_HEIGHT: int = 720
    GESTURE_DATABASE_PATH: str = 'gesture_database.json'
    CAMERA_FPS: int = 90
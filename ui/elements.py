from abc import ABC, abstractmethod
import cv2
import numpy as np
from typing import Tuple
from config.config import Config
from utils.logger import setup_logger

logger = setup_logger()

class UIElement(ABC):
    """Abstract base class for UI elements"""
    @abstractmethod
    def draw(self, frame: np.ndarray) -> None:
        pass

class Button(UIElement):
    """Interactive button element for the UI"""
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], text: str):
        self.position = position
        self.size = size
        self.text = text
        
    def draw(self, frame: np.ndarray) -> None:
        """Draw the button on the frame"""
        try:
            overlay = frame.copy()
            cv2.rectangle(overlay, self.position,
                         (self.position[0] + self.size[0], self.position[1] + self.size[1]),
                         Config.BUTTON_COLOR, -1)
            
            text_size = cv2.getTextSize(self.text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
            text_x = self.position[0] + (self.size[0] - text_size[0]) // 2
            text_y = self.position[1] + (self.size[1] + text_size[1]) // 2
            
            cv2.putText(overlay, self.text, (text_x, text_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, Config.BUTTON_TEXT_COLOR, 2)
            
            cv2.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)
        except Exception as e:
            logger.error(f"Error drawing button: {str(e)}")
            raise
        
    def contains_point(self, x: int, y: int) -> bool:
        """Check if a point is within the button's bounds"""
        return (self.position[0] <= x <= self.position[0] + self.size[0] and
                self.position[1] <= y <= self.position[1] + self.size[1])
"""
AI Controller for StyleMate AI

Coordinates all AI modules.
"""

from app.ai.vision import VisionEngine


class AIController:

    def __init__(self):
        self.vision = VisionEngine()

    def analyse(self, image):

        garment = self.vision.identify_garment(image)

        return {
            "garment": garment
        }
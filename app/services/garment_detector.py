"""
Garment Detector

This service will identify the type of garment
present in the uploaded image.

For now, it returns a placeholder result.
Later, we will replace this with a real AI model.
"""


def detect_garment(image):
    """
    Detect the garment type.

    Parameters:
        image: PIL Image

    Returns:
        Dictionary containing garment information.
    """

    return {
    "garment": "Unknown",
    "category": "Unknown",
    "primary_colour": "Unknown",
    "style": "Unknown",
    "pattern": "Unknown",
    "fabric": "Unknown",
    "season": [],
    "occasion": [],
    "confidence": 0.0
}
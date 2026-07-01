"""
Fashion Recommendation Engine

This module contains the logic for recommending
matching garments and accessories.
"""


def get_recommendations(garment_profile):
    """
    Returns fashion recommendations based on
    the garment profile.
    """

    garment = garment_profile.get("garment", "").lower()

    if garment == "shirt":
        return {
            "bottoms": [
                "Navy Chinos",
                "Beige Chinos",
                "Dark Blue Jeans"
            ],
            "footwear": [
                "Brown Loafers",
                "White Sneakers"
            ],
            "accessories": [
                "Brown Leather Belt",
                "Silver Watch"
            ],
            "reason": (
                "A shirt pairs well with chinos and dark denim "
                "for a smart and versatile look."
            )
        }

    return {
        "bottoms": [],
        "footwear": [],
        "accessories": [],
        "reason": "No recommendations available yet."
    }
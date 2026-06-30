from dataclasses import dataclass
from typing import List


@dataclass
class OutfitRecommendation:
    title: str
    occasion: str
    garments: List[str]
    footwear: List[str]
    accessories: List[str]
    reason: str
    score: int
from dataclasses import dataclass
from typing import List

@dataclass
class FashionProfile:
    garment_type: str
    category: str
    primary_color: str
    secondary_colors: List[str]
    pattern: str
    fabric: str
    fit: str
    style: str
    occasion: str
    season: str
    gender: str
    confidence: float
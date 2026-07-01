import json
from pathlib import Path


def load_matching_rules():
    """
    Load garment matching rules from JSON.
    """

    base_path = Path(__file__).resolve().parents[2]

    file_path = base_path / "data" / "fashion_rules" / "matching_rules.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
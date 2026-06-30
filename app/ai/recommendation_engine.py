from app.models.recommendation import OutfitRecommendation


class RecommendationEngine:

    def recommend(self, fashion_profile):

        return [
            OutfitRecommendation(
                title="Smart Casual",
                occasion="Office",
                garments=["Beige Chinos"],
                footwear=["Brown Loafers"],
                accessories=["Brown Belt", "Silver Watch"],
                reason="Classic complementary colour combination.",
                score=95
            )
        ]
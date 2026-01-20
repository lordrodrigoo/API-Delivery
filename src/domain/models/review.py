from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Review:
    """Entity of domain - it represents a review in the system."""
    id: Optional[int] = None
    order_id: Optional[int] = None
    user_id: Optional[int] = None
    rating: int
    comment: Optional[str] = None
    created_at: Optional[datetime] = None

    @property
    def is_positive(self) -> bool:
        """Check if the review is positive (rating 4 or 5)."""
        return self.rating >= 4

    @property
    def is_negative(self) -> bool:
        """Check if the review is negative (rating 1 to 3)."""
        return self.rating <= 3

    @staticmethod
    def create_review(
        order_id: int,
        user_id: int,
        rating: int,
        comment: Optional[str] = None
    ) -> 'Review':
        """Factory method to create a new Review."""
        return Review(
            order_id=order_id,
            user_id=user_id,
            rating=rating,
            comment=comment,
            created_at=datetime.utcnow()
        )

    @staticmethod
    def from_entity(entity) -> 'Review':
        """Converts a ReviewEntity to a Review domain model."""
        return Review(
            id=entity.id,
            order_id=entity.order_id,
            user_id=entity.user_id,
            rating=entity.rating,
            comment=entity.comment,
            created_at=entity.created_at
        )

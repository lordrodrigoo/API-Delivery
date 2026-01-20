from abc import ABC, abstractmethod
from src.domain.models.review import Review

class ReviewRepositoryInterface(ABC):
    """This interface defines the contract for review repository."""

    @abstractmethod
    def create_review(self, review: Review) -> Review: pass

    @abstractmethod
    def get_review_by_id(self, review_id: int) -> Review | None: pass

    @abstractmethod
    def find_reviews_by_user(self, user_id: int) -> list[Review]: pass

    @abstractmethod
    def find_reviews_by_rating(self, min_rating: int, max_rating: int) -> list[Review]: pass

    @abstractmethod
    def get_all_reviews(self) -> list[Review]: pass

    @abstractmethod
    def delete_review(self, review_id: int) -> bool: pass

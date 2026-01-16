from typing import Type, TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: Session):
        self.model = model
        self.session = session

    def add(self, obj: T) -> T:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def update(self, obj: T) -> T:
        self.session.merge(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def get_by_name(self, name: str) -> Optional[T]:
        return self.session.query(self.model).filter(self.model.name == name).first()

    def get_by_id(self, obj_id: int) -> Optional[T]:
        return self.session.query(self.model).get(obj_id)

    def get_all(self) -> List[T]:
        return self.session.query(self.model).all()

    def delete(self, obj: T) -> None:
        self.session.delete(obj)
        self.session.commit()

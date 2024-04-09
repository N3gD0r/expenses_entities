from abc import ABC, abstractmethod
from .entities import Entity, Expense, ExpenseCategory, User, ChatHistory
from typing import Any, Generic, TypeVar

T = TypeVar('T', bound=Entity)


class Repository(ABC, Generic[T]):
    @abstractmethod
    def __init__(self,
                 host: str,
                 user: str,
                 password: str,
                 db_name: str,
                 db_port: int):
        self._host = host
        self._user = user
        self._password = password
        self._db_name = db_name
        self._db_port = db_port

    @abstractmethod
    def get(self, id) -> T:
        pass

    @abstractmethod
    def get_by(self, **kwargs) -> list[T]:
        pass

    @abstractmethod
    def get_all(self) -> list[T]:
        pass

    @abstractmethod
    def add(self, entity: T) -> Any:
        pass

    @abstractmethod
    def update(self, id, entity: T) -> bool:
        pass

    @abstractmethod
    def delete(self, id) -> bool:
        pass


class ExpenseRepository(Repository[Expense]):

    @abstractmethod
    def get(self, id) -> Expense:
        pass

    @abstractmethod
    def get_by(self, **kwargs) -> list[Expense]:
        pass

    @abstractmethod
    def get_all(self) -> list[Expense]:
        pass

    @abstractmethod
    def add(self, entity: Expense) -> Any:
        pass

    @abstractmethod
    def update(self, id, entity: Expense) -> bool:
        pass

    @abstractmethod
    def delete(self, id) -> bool:
        pass


class ExpenseCategoriesRepository(Repository[ExpenseCategory]):

    @abstractmethod
    def get(self, id) -> ExpenseCategory:
        pass

    @abstractmethod
    def get_by(self, **kwargs) -> list[ExpenseCategory]:
        pass

    @abstractmethod
    def get_all(self) -> list[ExpenseCategory]:
        pass

    @abstractmethod
    def add(self, entity: ExpenseCategory) -> Any:
        pass

    @abstractmethod
    def update(self, id, entity: ExpenseCategory) -> bool:
        pass

    @abstractmethod
    def delete(self, id) -> bool:
        pass


class UserRepository(Repository[User]):

    @abstractmethod
    def get(self, id) -> User:
        pass

    @abstractmethod
    def get_by(self, **kwargs) -> [User]:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def add(self, entity: User) -> Any:
        pass

    @abstractmethod
    def update(self, id, entity: User) -> bool:
        pass

    @abstractmethod
    def delete(self, id) -> bool:
        pass


class ChatHistoryRepository(Repository[ChatHistory]):

    @abstractmethod
    def get(self, id) -> ChatHistory:
        pass

    @abstractmethod
    def get_by(self, **kwargs) -> list[ChatHistory]:
        pass

    @abstractmethod
    def get_all(self) -> list[ChatHistory]:
        pass

    @abstractmethod
    def add(self, entity: ChatHistory) -> Any:
        pass

    @abstractmethod
    def add_batch(self, entities: list[ChatHistory]) -> Any:
        pass

    @abstractmethod
    def update(self, id, entity: ChatHistory) -> bool:
        pass

    @abstractmethod
    def delete(self, id) -> bool:
        pass

    @abstractmethod
    def delete_batch(self, chat_ids: list[Any]) -> bool:
        pass


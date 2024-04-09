from abc import ABC
from dataclasses import dataclass
from datetime import date


@dataclass(kw_only=True)
class Entity(ABC):
    status: bool = True
    created_at: date = date.today()
    updated_at: date = date.today()

    def get_dict(self):
        return self.__dict__


@dataclass(kw_only=True)
class Expense(Entity):
    expense_id: int = None
    expense_amount: float
    expense_name: str
    month_year: date
    exp_category_id: int
    category_name: str = None
    user_id: int


@dataclass(kw_only=True)
class ExpenseCategory(Entity):
    exp_category_id: int
    category_name: str


@dataclass(kw_only=True)
class User(Entity):
    user_id: int = None
    username: str
    password: str


@dataclass(kw_only=True)
class ChatHistory(Entity):
    chat_id: int = None
    user_id: int
    role_id: int
    content: str


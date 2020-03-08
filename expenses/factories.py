# Factory
import factory
from factory import Faker
from factory.django import DjangoModelFactory

# Models
from expenses.models import Expense


class ExpenseFactory(DjangoModelFactory):
    pass
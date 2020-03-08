# Django
from django.contrib.auth import get_user_model

# Factory
import factory
from factory import Faker
from factory.django import DjangoModelFactory

# Models
from expenses.models import Expense

User = get_user_model()

class UserFactory(factory.Factory):
    class Meta:
        model = User
        
    first_name = factory.Faker('name')
    username = factory.lazy_attribute(lambda o: '%s' % o.first_name)
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.first_name)


class ExpenseFactory(DjangoModelFactory):
    class Meta:
        model = Expense

    user = User.objects.last()
    name = factory.Sequence(lambda n: 'Compra impulsiva #%03s' % n)
    cost = 250.00
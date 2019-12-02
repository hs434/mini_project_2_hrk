# 1 - imports
from base import Session, engine, Base
from sqlalchemy.orm import  sessionmaker, Session

from base import Customer
from pprint import pprint



# 2 - generate database schema
Base.metadata.create_all(engine)
Base.metadata.bind = engine

# 3 - create a new session
session = Session()

# 4 - create Customer
c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )


print(c1.first_name , c1.last_name)
print(c2.first_name , c2.last_name)
session.add(c1)
session.add(c2)
print(c1.id)
print(c2.id)
session.add_all([c1, c2])
session.new
pprint(session.new)
pprint(engine.table_names())
# 10 - commit and close session
session.commit()
print(c1.id , c2.id)

c3 = Customer(
    first_name="John",
    last_name="Lara",
    username="johnlara",
    email="johnlara@mail.com",
    address="3073 Derek Drive",
    town="Norfolk"
    )

c4 = Customer(
    first_name="Sarah",
    last_name="Tomlin",
    username="sarahtomlin",
    email="sarahtomlin@mail.com",
    address="3572 Poplar Avenue",
    town="Norfolk"
    )

c5 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c6 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add_all([c3, c4, c5, c6])
session.commit()
print(c3.first_name, c4.first_name, c5.first_name,  c6.first_name)
session.close()

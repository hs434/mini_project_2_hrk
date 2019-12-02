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
session.close()

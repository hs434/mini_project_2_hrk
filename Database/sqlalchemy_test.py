from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker, Session
from datetime import datetime
from sqlalchemy import *
from  pprint import pprint
from sqlalchemy import desc
from sqlalchemy import func



engine = create_engine("sqlite:////web/Sqlite-Data/mydb.db")
Base = declarative_base()



class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(Integer(), nullable=False)
    orders = relationship("OrderLine", backref='item')
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship("OrderLine", backref='order')
class OrderLine(Base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())


#Base.metadata.drop_all(engine)
# 2 - generate database schema
Base.metadata.create_all(engine)
Base.metadata.bind = engine

# 3 - create a new session
session = Session(bind=engine)

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
session.add(c1)
session.add(c2)
session.commit()



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

#add some products to the items table
i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price= 3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price= 15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price= 20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price= 200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price= 100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
item = [i1, i2, i3, i4, i5, i6, i7, i8]
session.commit()

#Create some orders now:
o1 = Order(customer=c1)
o2 = Order(customer=c1)

line_item1 = OrderLine(order=o1, item=i1, quantity=3)
line_item2 = OrderLine(order=o1, item=i2, quantity=2)
line_item3 = OrderLine(order=o2, item=i1, quantity=1)
line_item3 = OrderLine(order=o2, item=i2, quantity=4)

session.add_all([o1, o2])
session.new
orders = [o1, o2]
session.commit()

#o3 = Order(customer=c1)
#orderline1 = OrderLine(item=i1, quantity=5)
#orderline2 = OrderLine(item=i2, quantity=10)

#o3.order_lines.append(orderline1)
#o3.order_lines.append(orderline2)

#session.add_all([o3])
#session.commit()

pprint("Below Data for session.query(Customer).all()")
result = session.query(Customer).all()
for row in result:
   print ("Name: ",row.first_name ,","  ,row.last_name ," Address: ",row.address, " Email: ",row.email)

pprint("Below Data for session.query(Item).all()")
result = session.query(Item).all()
for row in result:
   print ("Name: ",row.name)

pprint("Below Data for session.query(Order).all()")
result = session.query(Order).all()
for row in result:
   print ("Order: ",row.id)

pprint("Below Data for session.query(Customer)")
print(session.query(Customer))

pprint("Below Data with for loop for session.query(Customer)")
q = session.query(Customer)
for c in q:
    print(c.id, c.first_name)

pprint("Below Data for session.query(Customer.id, Customer.first_name).all()")
print(session.query(Customer.id, Customer.first_name).all())


pprint("Below Data for count() method")
print(session.query(Customer).count())
print(session.query(Item).count())
print(session.query(Order).count())

pprint("Below Data for first() method")
c = session.query(Customer).first()
print("Customer:",c.id,'-',c.first_name)
i = session.query(Item).first()
print("Item:",i.id,'-',i.name)
o =session.query(Order).first()
print("Order:",o.id)


pprint("Below Data for get() method")
c = session.query(Customer).get(1)
print("Customer:",c.id,'-',c.first_name)
i = session.query(Item).get(1)
print("Item:",i.id,'-',i.name)
print(session.query(Order).get(100))


pprint("Below Data for filter() method")
q = session.query(Customer).filter(Customer.first_name == 'John').all()
for c in q:
 print("Customer:",c.id,'-',c.first_name,c.last_name)

pprint("Below sql equivalent for filter() method")
print(session.query(Customer).filter(Customer.first_name == 'John'))

pprint("Below sql equivalent for multiple filters to the filter() method")
print(session.query(Customer).filter(Customer.id <= 5, Customer.town.like("Nor%")))

pprint("Below Data for all customers who either live in Peterbrugh or Norfolk")
q = session.query(Customer).filter(or_(
    Customer.town == 'Peterbrugh',
    Customer.town == 'Norfolk'
)).all()
for c in q:
 print("Customer:",c.id,'-',c.first_name,c.last_name)

 pprint("Below Data for all customers whose first name is John and live in Norfolk")
 q = session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    Customer.town == 'Norfolk'
)).all()
 for c in q:
     print("Customer:", c.id, '-', c.first_name, c.last_name)

 pprint("Below Data for all johns who don't live in Peterbrugh")
 q = session.query(Customer).filter(and_(
    Customer.first_name == 'John',
    not_(
        Customer.town == 'Peterbrugh',
    )
)).all()
 for c in q:
     print("Customer:", c.id, '-', c.first_name, c.last_name)

pprint("Below Data is for IS NULL")
q = session.query(Order).filter(Order.date_placed == None).all()
for o in q:
    print("Order: ", o.id)

pprint("Below Data is for IS NOT NULL")
q = session.query(Order).filter(Order.date_placed != None).all()
for o in q:
    print("Order: ", o.id)

pprint("Below Data is for IN")
q = session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all()
for c in q:
    print("Customer: ",c.id,"-", c.first_name,c.last_name)

pprint("Below Data is for NOT IN")
q = session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all()
for c in q:
    print("Customer: ",c.id,"-", c.first_name,c.last_name)

pprint("Below Data is for BETWEEN")
q =	session.query(Item).filter(Item.cost_price.between(10, 50)).all()
for i in q:
    print("Item: ",i.id,"-", i.name)

pprint("Below Data is for NOT BETWEEN")
q =	session.query(Item).filter(not_(Item.cost_price.between(10, 50))).all()
for i in q:
    print("Item: ",i.id,"-", i.name)

pprint("Below Data is for LIKE")
q =	session.query(Item).filter(Item.name.like("%r")).all()
for i in q:
    print("Item: ",i.id,"-", i.name)

pprint("Below Data is for iLIKE")
q =	session.query(Item).filter(Item.name.ilike("w%")).all()
for i in q:
    print("Item: ",i.id,"-", i.name)

pprint("Below Data is for NOT LIKE")
q =	session.query(Item).filter(not_(Item.name.like("W%"))).all()
for i in q:
    print("Item: ",i.id,"-", i.name)

pprint("Below Data is for limit() method")
q =	session.query(Customer).limit(2).all()
for c in q:
    print("Customer: ", c.id, "-", c.first_name, c.last_name)

pprint("Below Data is for limit() method with ilike")
q =	session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2).all()
for c in q:
    print("Customer: ", c.id, "-", c.first_name, c.last_name)

pprint("Below Data is for sql equivalent for limit() method")
print(session.query(Customer).limit(2))
print(session.query(Customer).filter(Customer.address.ilike("%avenue")).limit(2))

pprint("Below Data is for offset() method")
q =	session.query(Customer).limit(2).offset(2).all()
for c in q:
    print("Customer: ", c.id, "-", c.first_name, c.last_name)

pprint("Below Data is for sql equivalent for limit() method")
print(session.query(Customer).limit(2).offset(2))

pprint("Below Data is for order_by() method")
q =	session.query(Item).filter(Item.name.ilike("wa%")).all()
for i in q:
    print("Item: ", i.id, "-", i.name)

pprint("Below Data is for order_by() method")
q =	session.query(Item).filter(Item.name.ilike("wa%")).order_by(Item.cost_price).all()
for i in q:
    print("Item: ", i.id, "-", i.name)

pprint("Below Data is for desc() function")
q =	session.query(Item).filter(Item.name.ilike("wa%")).order_by(desc(Item.cost_price)).all()
for i in q:
    print("Item: ", i.id, "-", i.name)


pprint("Below Data is for join() method")
q =	session.query(Customer).join(Order).all()
for c in q:
    print("Customer: ", c.id, "-", c.first_name, c.last_name)

pprint("Below Data is for sql equivalent for join() method")
print(session.query(Customer).join(Order))

pprint("Below Data is for one or more table in a single query")
pprint(session.query(Customer.id, Customer.username, Order.id).join(Order).all())

pprint("Below Data is for outerjoin()")
q =	session.query(
    Customer.first_name,
    Order.id,
).outerjoin(Order).all()
for c in q:
    print(c.first_name,   c.id)

pprint("Below Data is for group_by() method")
print(session.query(func.count(Customer.id)).join(Order).filter(
    Customer.first_name == 'John',
    Customer.last_name == 'Green',
).group_by(Customer.id).scalar())


pprint("Below Data is for having() method")
print(session.query(
    func.count("*").label('town_count'),
    Customer.town
).group_by(Customer.town).having(func.count("*") >= 2).all())
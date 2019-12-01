from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, ForeignKey, Numeric, SmallInteger, Integer, String
from datetime import datetime
from sqlalchemy.orm import relationship
# Create an engine that stores data in the local directory's
# mydb.db file.
engine = create_engine('sqlite:////web/Sqlite-Data/mydb.db')

# this loads the sqlalchemy base class
Base = declarative_base()

# Setting up the classes that create the record objects and define the schema
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(200), nullable=False)
  #  created_on = Column(DateTime(), default=datetime.now)
   # updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    #orders = relationship("Order", backref='customer')

    def __init__(self, first_name, last_name,username,email,address,town):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.address = address
        self.town = town
     #   self.created_on = created_on
      #  self.updated_on = updated_on
       # self.orders = orders
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.

Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
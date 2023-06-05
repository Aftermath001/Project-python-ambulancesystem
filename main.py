from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class Patient(Base):
    __tablename__ = 'patients'
    id = Column (Integer(), primary_key= True)
    firstName = Column(String())
    lastName = Column(String())
    level = Column(Integer())
    # reviews = relationship('Review', backref=backref('customer'))
    def __repr__(self):
        return f'Patient(id = {self.id})'+\
           f'firstName = {self.firstName}'+\
           f'lastName={self.lastName}' +\
           f'level ={self.level}'
    
class Driver(Base):
    __tablename__ = 'drivers'
    id = Column (Integer(), primary_key=True)
    name = Column(Integer())
    # customer_id = Column(Integer(), ForeignKey('customers.id'))
    # restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    def __repr__(self):
        return f'Driver(id = {self.id})'+\
           f'name = {self.rating}'
        #    f'customer_id={self.customer_id}'

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer(), primary_key= True)
    car_model = Column(String())
    # reviews = relationship('Review', backref=backref('restaurant'))
    def __repr__ (self):
        return f' Vehicle(id = {self.id})'+\
            f'car_model={self.car_model}'
if __name__ == '__main__':
    engine = create_engine('sqlite:///records.db')
    Base.metadata.create_all(engine)
     # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()
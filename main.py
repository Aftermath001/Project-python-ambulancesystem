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
    description = Column(String())
    level = Column(Integer())

    drivers = relationship('Driver', backref=backref('patient'))

    def __repr__(self):
        return f'Patient(id = {self.id})'+\
           f'firstName = {self.firstName}'+\
           f'lastName={self.lastName}' +\
           f'description ={self.description}'+\
           f'level ={self.level}'

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer(), primary_key= True)
    registration = Column(String())
    drivers = relationship('Driver', backref=backref('vehicle'))
    
    def __repr__ (self):
        return f' Vehicle(id = {self.id})'+\
            f'registration={self.registration}'



class Driver(Base):
    __tablename__ = 'drivers'
    id = Column (Integer(), primary_key=True)
    name = Column(Integer())

    patient_id = Column(Integer(), ForeignKey('patients.id'))
    vehicle_id = Column(Integer(), ForeignKey('vehicles.id'))
    def __repr__(self):
        return f'Driver(id = {self.id})'+\
           f'name = {self.name}'+\
           f'patient_id={self.patient_id}'+\
           f'vehicle_id={self.vehicle_id}'
       


    

class Hospital(Base):
    __tablename__ = 'hospitals'
    id = Column(Integer(), primary_key= True)
    name = Column(String())
    location= Column(String())
    def __repr__ (self):
        return f' Hospital(id = {self.id})'+\
            f'name={self.name}'+\
            f'location = {self.location}'
    
if __name__ == '__main__':
    engine = create_engine('sqlite:///records.db')
    Base.metadata.create_all(engine)
     # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()

#Patient's instances
    patient1 = Patient(
        firstName ="Alvin",
        lastName ="Adams",
        description ="I have mild headaches and back pains",
        level = 1
        )
    patient2 = Patient(
        firstName ="Jephat",
        lastName ="Maina",
        description = "Frequent diaarhoea and vomiting",
        level = 3
        )
    patient3 = Patient(
        firstName ="Orina",
        lastName ="Ephy",
        description ="Fresh cut from a sharp object",
        level = 2
        )
    patient4 = Patient(
        firstName ="Kimani",
        lastName ="Bonnke",
        description = "Internal bleeding, body paleness",
        level = 5
        )
    
    # Driver's Instances
    driver1 = Driver(
        name = "Teddy Makarios",
        patient_id = 1,
        vehicle_id = 3
        )
    driver2 = Driver(
        name = "Thanos Imani",
        patient_id = 1,
        vehicle_id = 3
        )
    driver3 = Driver(
        name = "Mkadin Ale",
        patient_id = 1,
        vehicle_id = 3
        )
    driver4 = Driver(
        name = "James Kamau",
        patient_id = 1,
        vehicle_id = 3
        )
    driver5 = Driver(
        name = "Mishy Dora",
        patient_id = 1,
        vehicle_id = 3
        )
    driver6 = Driver(
        name = "Huddah Munroe"
        )
    
    # Vehicle Instances
    vehicle1 = Vehicle(
        registration = "KAR-275J"
        )
    vehicle2 = Vehicle(
        registration = "KBC-350V"
        )
    vehicle3 = Vehicle(
        registration = "KBE-415R"
        )
    vehicle4 = Vehicle(
        registration = "KAZ-150C"
        )
    vehicle5 = Vehicle(
        registration = "KDC-200V"
        )
    
    # Hospital Instances
    hospital1 = Hospital(
        name = "Kenyatta Hospital",
        location = "Kenyatta"
    )
    hospital2 = Hospital(
        name = "Mp Shah",
        location = "Parklands"
    )
    hospital3 = Hospital(
        name = "Mata Hospital",
        location = "Eastlands"
    )
    hospital4 = Hospital(
        name = "Nairobi West",\
        location = "Westlands"
    )
    
    session.add_all([patient1, patient2,patient3,patient4])
    session.add_all([driver1, driver2,driver3,driver4,driver5,driver6])
    session.add_all([vehicle1, vehicle2,vehicle3,vehicle4,vehicle5])
    session.add_all([hospital1, hospital2,hospital3,hospital4])

    session.commit()
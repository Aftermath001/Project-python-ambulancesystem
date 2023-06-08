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
    
    hospitals = relationship ('Hospital', backref=backref('patient'))
    
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
    location = Column(String())
    drivers = relationship('Driver', backref=backref('vehicle'))
    
    def __repr__ (self):
        return f' Vehicle(id = {self.id})'+\
            f'registration={self.registration}'+\
            f'location = {self.location}'



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
    hotLine =  Column(Integer())
#    Relationships
    patient_id = Column(Integer(), ForeignKey('patients.id'))
    
    def __repr__ (self):
        return f' Hospital(id = {self.id})'+\
            f'name={self.name}'+\
            f'location = {self.location}'+\
            f'patient_id = {self.patient_id}'
    
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
    patient5 = Patient(
        firstName ="Minayo",
        lastName ="Victoria",
        description = "Internal bleeding, body paleness",
        level = 4
        )
    patient6 = Patient(
        firstName ="Waka",
        lastName ="Joy",
        description = "Internal bleeding, body paleness",
        level = 3
        )
    
    
    # Driver's Instances
    driver1 = Driver(
        name = "Teddy Makarios",
        patient_id = 1,
        vehicle_id = 2
        )
    driver2 = Driver(
        name = "Thanos Imani",
        patient_id = 3,
        vehicle_id = 1
        )
    driver3 = Driver(
        name = "Mkadin Ale",
        patient_id = 4,
        vehicle_id = 5
        )
    driver4 = Driver(
        name = "James Kamau",
        patient_id = 5,
        vehicle_id = 2
        )
    driver5 = Driver(
        name = "Mishy Dora",
        patient_id = 6,
        vehicle_id = 3
        )
    driver6 = Driver(
        name = "Huddah Munroe",
        patient_id = 2,
        vehicle_id = 4
        )
    
    # Vehicle Instances
    vehicle1 = Vehicle(
        registration = "KAR-275J",
        location = "Kenyatta"
        )
    vehicle2 = Vehicle(
        registration = "KBC-350V",
        location = "Parklands"
        )
    vehicle3 = Vehicle(
        registration = "KBE-415R",
        location = "Kenyatta"
        )
    vehicle4 = Vehicle(
        registration = "KAZ-150C",
        location = "Eastlands"
        )
    vehicle5 = Vehicle(
        registration = "KBV-420V",
        location = "Kajiado"
        )
    vehicle6 = Vehicle(
        registration = "KAS-975J",
        location = "Adams Arcade"
        )
    vehicle7 = Vehicle(
        registration = "KXY-469L",
        location = "Kajiado"
        )
    vehicle8 = Vehicle(
        registration = "KAZ-350F",
        location = "Westlands"
        )
    
    # Hospital Instances
    hospital1 = Hospital(
        name = "Kenyatta Hospital",
        location = "Kenyatta",
        hotLine = 452
    )
    hospital2 = Hospital(
        name = "Mp Shah",
        location = "Parklands",
        hotLine = 708
    )
    hospital3 = Hospital(
        name = "Mata Hospital",
        location = "Eastlands",
        hotLine = 254
    )
    hospital4 = Hospital(
        name = "Aga Khan",
        location = "Kajiado",
        hotLine= 432
    )
    hospital5 = Hospital(
        name = "Mata Hospital",
        location = "Westlands",
        hotLine= 500
    )
    hospital6 = Hospital(
        name = "Iran Hospital",
        location = "Adams Arcade",
        hotLine= 575
    )
    hospital7 = Hospital(
        name = "King David",
        location = "Kajiado",
        hotLine= 990
    )
    hospital8= Hospital(
        name = "Aga Khan",
        location = "Westlands",
        hotLine= 483
    )
    session.add_all([patient1, patient2,patient3,patient4])
    session.add_all([driver1, driver2,driver3,driver4,driver5,driver6])
    session.add_all([vehicle1, vehicle2,vehicle3,vehicle4,vehicle5,vehicle6,vehicle7,vehicle8])
    session.add_all([hospital1, hospital2,hospital3,hospital4,hospital5,hospital6,hospital7,hospital8])

    session.commit()


# Menu details
def main():

    option = 0
    while option != 4:
        print("***MENU***")
        print("1)Get a list of all hospitals")
        print("2)Select hospital of choice")
        print("3)Select your location")
        print("4)Leave Menu")
        
        option = int(input())

        if option == 1:
        
          hospitals_list = session.query(Hospital).all()
          hospitals_list.append([])
          for hospitals in hospitals_list:
            print(hospitals)



#   ***** Print a list ***** 
        elif option == 2:
            print ("Select hospital of choice")
            user_input = input("Enter the hospital name:")
            hospitals = session.query(Hospital).filter(Hospital.name == user_input)
            for hospital in hospitals:
              print ([hospital.id, hospital.name, hospital.location, hospital.hotLine])


# Print a tuple
        elif option == 3:
            print ("Select the location")
            user_input = input("Enter the location:")
            for hospital , vehicle in session.query(Hospital, Vehicle).filter(Hospital.location== user_input, Vehicle.location == user_input):
                print(("ID=",hospital.id,"Name=", hospital.name,"Location=", hospital.location, "Hotline:",hospital.hotLine,"Number Plate=",vehicle.registration))
            
              

        elif option == 4:
            print("Thank You, Leaving Menu")

        else:
            print("Invalid input")
            

           

if __name__ == "__main__":
    main()
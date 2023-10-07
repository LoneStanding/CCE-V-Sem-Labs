class Vehicle:

    def __init__(self,owner, vehicleID, manufacturer):
        self.owner = owner
        self.vehicleID = vehicleID
        self.manufacturer = manufacturer

    def disp(self):
        print ("Owner: ", self.owner)
        print ("VehicleID: ", self.vehicleID)
        print ("Manufacturer: ", self.manufacturer)

class Passenger(Vehicle):

    def __init__(self,v,NoOfPassengers):
        self.n = NoOfPassengers
        self.owner = v.owner
        self.vehicleID = v.vehicleID
        self.manufacturer = v.manufacturer

    def disp(self):
        print ("NoOfPassengers: ", self.n)

own, vehid, manfac, passenger = (input("Enter Vehicle information").split(" "))

v = Vehicle(own, vehid, manfac)
psgr = Passenger(v,passenger)

v.disp()
psgr.disp()
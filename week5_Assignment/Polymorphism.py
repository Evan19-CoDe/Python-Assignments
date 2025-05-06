# Class
class Vehicles:
    def move(self):
        print("The vehicles is moving.")
        
# Child class
class Car(Vehicles):
    def move(self):
        print("driving on the tarmac.")
        
class WaterBoat(Vehicles):
    def move(self):
        print("Sailing on the sea.")
    
class Aeroplane(Vehicles):
    def move(self):
        print("Flying in the sky.")
        
# A list of Vehicles
Vehicles = [Car(), WaterBoat(), Aeroplane()]

# Loop through and call move()
for V in Vehicles:
    V.move()        

        
        
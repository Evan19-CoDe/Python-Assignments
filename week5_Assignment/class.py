# Class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.strength_level = strength_level
    
    def show_power(self):
        print(f"{self.name}uses {self.power} with stregth level {self.strength_level}!")

# Inherited Class 1.
class FlyingHero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed
        
    def show_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h and uses {self.power}!")

# Inherited Class 2.
class StrengthHero(Superhero):
    def __init__(self, name, power, strength_level, lift_capacity):
        super().__init__(name, power, strength_level)
        self.lift_capacity = lift_capacity
        
    def show_power(self):
        print(f"{self.name} lift {self.lift_capacity} tons while using {self.power}!")
        
# Objects
hero1 = FlyingHero("Appa", "Tornado Twirl", 100, 450)
hero2 = StrengthHero("MoMo", "Bound Fist", 105, 70)

# Call Methods
hero1.show_power()
hero2.show_power()
class Vehicle:
    def __init__(self, wheels, seats, colour, tank_size, distance_on_full_tank):
        self.distance = None
        self.wheels = wheels
        self.seats = seats
        self.colour = colour
        self.tank_size = tank_size
        self.distance_on_full_tank = distance_on_full_tank

    def distance_per_litre(self):
        distance = self.distance_on_full_tank / self.tank_size
        return distance


joseph = Vehicle(6, 4, "Blue", 600, 20000)

# print(f"{joseph.distance_per_litre()} km per litre")
print(joseph)
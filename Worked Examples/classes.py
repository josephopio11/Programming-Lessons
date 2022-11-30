class Vehicle:
    vehicle_id = ""
    registration = ""
    date_of_registration = ""
    engine_size = 0
    purchase_price = 0


new_car = Vehicle()
new_car.vehicle_id = 1
new_car.registration = "ABC123"
new_car.date_of_registration = "01/01/2019"
new_car.engine_size = 1.2
new_car.purchase_price = 10000

print(new_car.registration)

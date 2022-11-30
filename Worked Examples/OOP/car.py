class Car:
    def __init__(self, vehicle_id, engine_size):
        self.tyres = None
        self.registration = None
        self.purchase_price = None
        self.date_of_registration = None
        self.vehicle_id = vehicle_id
        self.engine_size = engine_size

    def set_purchase_price(self, purchase_price):
        self.purchase_price = purchase_price
        return self.purchase_price

    def set_registration(self, registration):
        self.registration = registration
        return registration

    def set_no_of_tyres(self, tyres):
        self.tyres = tyres
        return tyres

    def set_date_of_registration(self, date_of_registration):
        self.date_of_registration = date_of_registration
        return

    def get_vehicle_id(self):
        return self.vehicle_id

    def get_registration(self):
        return self.registration

    def get_date_of_registration(self):
        return self.date_of_registration

    def get_engine_size(self):
        return self.engine_size

    def get_purchase_price(self):
        return self.purchase_price

    def get_no_of_tyres(self):
        return self.tyres


class BMW(Car):
    def __init__(self, vehicle_id, engine_size):
        super().__init__(vehicle_id, engine_size)
        self.date_hired = None

    def when_hired(self, date_hired):
        self.date_hired = date_hired
        return date_hired

    class Engine:
        def __init__(self, piston):
            self.piston = piston

        class Piston:
            def __init__(self, manufacturer):
                self.manufacturer = manufacturer

    class Tyres:
        def __init__(self, size, date_of_expiry):
            self.size = size
            self.date_of_expiry = date_of_expiry

#
new_car = BMW()
#
# taken = new_car.when_hired('16-11-2022')
#
# my_tyre = new_car.Tyres(24, '31-01-2032')
#
# print(my_tyre.date_of_expiry)
# print(taken)

# peugeot.set_registration('UBJ 123A')
# peugeot.set_purchase_price(2000)
# bmw.set_purchase_price(3000)
#
# print(bmw.get_purchase_price())
# print(peugeot.get_engine_size())

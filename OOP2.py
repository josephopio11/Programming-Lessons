class Car:
    def __init__(self, v, e):
        self.__VehicleId = v
        self.__EngineSize = e
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__PurchasePrice = 0.00
    @property
    def VehicleId(self):
        return self.__VehicleId

    @property
    def EngineSize(self):
        return self.__EngineSize

    @property
    def Registration(self):
        return self.__Registration

    @property
    def DateOfRegistration(self):
        return self.__DateOfRegistration

    @property
    def PurchasePrice(self):
        return self.__PurchasePrice

    @Registration.setter
    def Registration(self, r):
        self.__Registration = r

    @DateOfRegistration.setter
    def DateOfRegistration(self, d):
        self.__DateOfRegistration = d

    @PurchasePrice.setter
    def PurchasePrice(self, p):
        self.__PurchasePrice = p


MyCar = Car("123ABC", 2400)
WifeysCar = Car("135JPQ", 1200)

MyCar.Registration = "ASC321"

print(MyCar.Registration)
print(MyCar.VehicleId)


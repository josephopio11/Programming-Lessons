# VehicleID
# Registration
# DateOfRegistration
# EngineSize
# PurchasePrice
#
# Constructor
# SetPurchasePrice
# SetRegistrationNumber
# SetDateOfRegistration
#
# GetRegistration
# GetPurchasePrice
# GetDateOfRegistration
# GetEngineSize

class Car:
    def __init__(self, v, e):
        self.__VehicleId = v
        self.__EngineSize = e
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__PurchasePrice = 0.00

    def SetPurchasePrice(self, NewPurchasePrice):
        self.__PurchasePrice = NewPurchasePrice

    def SetRegistrationNumber(self,NewRegistrationNumber):
        self.__Registration = NewRegistrationNumber

    def SetDateOfRegistration(self, NewDateOfRegistration):
        self.__DateOfRegistration = NewDateOfRegistration

    def GetRegistration(self):
        return self.__Registration

    def GetPurchasePrice(self):
        return self.__PurchasePrice

    def GetDateOfRegistration(self):
        return self.__DateOfRegistration

    def GetEngineSize(self):
        return self.__EngineSize



MyCar = Car("123ABC", 2400)
WifeysCar = Car("135JPQ", 1200)

MyCar.SetRegistrationNumber("890ryue")
print(MyCar.GetRegistration())
print(MyCar.GetEngineSize())
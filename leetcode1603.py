class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigStorage = big
        self.mediumStorage = medium
        self.smallStorage = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.bigStorage >= 1:
            self.bigStorage -= 1
            print("big")
            return True
        if carType == 2 and self.mediumStorage >= 1:
            self.mediumStorage -= 1
            print("mid")
            return True
        if carType == 3 and self.smallStorage >= 1:
            self.smallStorage -= 1
            print("small")
            return True
        else:
            print("no room")
            return False


ParkingSystem = ParkingSystem(1,1,0)
ParkingSystem.addCar(1)
ParkingSystem.addCar(2)
ParkingSystem.addCar(3)



class car:
    @staticmethod
    def start():
        print("car is starting....")
    @staticmethod
    def stop():
        print("car is stoping....")

class toyota(car):
    def __init__(self,brand):
        self.brand="purise"


class fornutner(toyota):
    def __init__(self,type):
        self.type=type

car1=fornutner("dieasel")        

car1.start()
car1.stop()

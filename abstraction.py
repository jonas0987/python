class car:
    def __init__(self):
        
        self.acc=False
        self.brake=False
        self.cluth=False

    def start(self):
        self.acc=True
        self.cluth=True
        print("car getting started.....")

c1=car()
c1.start()        


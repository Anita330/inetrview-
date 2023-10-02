class train:
    def __init__(self,name,fare,seat): 
        self.name = name
        self.fare = fare
        self.seat = seat
    def getstatus(self):
        print(f" the name of the train is {self.name}")
        print(f"tha available seats is {self.seat}")

    def fareinfo(self):
        print(f"the price of ticket is {self.fare}")


intercity = train("inetrcity express :14023" ,90 , 300)
intercity.getstatus()
intercity.fareinfo()
class Time:
    def __init__(self):
        self.__hour=int(input("enter the hour:"))
        self.__minute=int(input("enter the minute:"))
        self.__second=int(input("enter the second:"))

    def __add__(self,other):

        seconds=(self.__second + other.__second)%60
        minutes=(self.__minute + other.__minute)%60 + (self.__second + other.__second)//60
        hours=(self.__hour + other.__hour)%60 + (self.__minute + other.__minute)//60


        print("\n-----------AFTER TIME ADDITION----------------")
        print(seconds,":",minutes,":",hours)
              

t1=Time()
t2=Time()


t1 + t2


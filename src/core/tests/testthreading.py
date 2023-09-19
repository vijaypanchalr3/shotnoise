import time
import multiprocessing
from threading import Thread
class titan:
    def __init__(self) -> None:
        self.food = 450
        pass
    def foo(self):
        # maybe you should do a loop here?
        while True:

            # normally, you should alter instance property rather than class property.
            # so it's better to update self.food, rather than titan.food .
            self.food = self.food - 10
            print(self.food, 'food left')
            time.sleep(.5)
            # maybe you want to exit if food is <0?
            if self.food < 0:
                break

    def ask(self):
        # maybe you also want a loop here?
        while True:
            print("hello")
            if input == 'y':
                self.food = self.food + 100
                print('food refilled!----->>>>', self.food)
            elif input == 'n':
                pass
            else:
                break
            # shouldn't use elif here, because if food < 0,
            # it will also satisfy food<400, 
            # thus the elif block will never be executed.
            if self.food < 0:
                print("My time has come !!! +  ")
                break
       

a = titan()

p1 =  Thread(target=a.foo())
p2 =  Thread(target=a.ask())
p1.start()
p2.start()
p1.join()
p2.join()

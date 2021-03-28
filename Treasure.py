import random
class Treasure:
    def __init__(self):
        type=random.randint(1,2)
        self.creat_treasure(type)
    def creat_treasure(self,type):
        if type==1:
            self.name="木剑"
            self.attack_max=5
            self.attack_min=1
            self.level=2
            self.belonging=0
        if type==2:
            self.name="铜剑"
            self.attack_max=10
            self.attack_min=5
            self.level=5
            self.belonging=0
if __name__ == '__main__':
    Treasure=Treasure()
    print(Treasure.name)




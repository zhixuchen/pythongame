import random
import treasure

class Monster:
    def __init__(self):
        type = random.randint(1, 2)
        self.creat_monster(type)

    def creat_monster(self, type):
        if type == 1:
            self.name = "神兽1"
            self.blood_volume = 1000  # 血量
            self.curr_blood_volume = 1000  # 当前血量
            self.defense = 20  # 防御
            self.experience = 100  # 经验
            self.attack_max = 30  # 最大攻击力
            self.attack_min = 10  # 最小攻击力
        if type == 2:
            self.name = "神兽2"
            self.blood_volume = 3000  # 血量
            self.curr_blood_volume = 3000  # 当前血量
            self.defense = 40  # 防御
            self.experience = 200  # 经验
            self.attack_max = 60  # 最大攻击力
            self.attack_min = 20  # 最小攻击力

    def add_curr_blood_volume(self, add):
        self.curr_blood_volume = self.curr_blood_volume + add
        if self.curr_blood_volume > self.blood_volume:
            self.curr_blood_volume = self.blood_volume
        return True

    def cut_curr_blood_volume(self, cut):
        self.curr_blood_volume = self.curr_blood_volume - cut
        if self.curr_blood_volume <= 0:
            self.die()

    def die(self):
        print(self.name + "死了")
        Treasure=treasure.Treasure()
        Treasure.belonging=1
        print(Treasure.name)




if __name__ == '__main__':
    Monster = Monster()
    print("当前血量：" + str(Monster.curr_blood_volume))
    Monster.cut_curr_blood_volume(2000)

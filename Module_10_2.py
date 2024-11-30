from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power
    def run(self):
        enemy_power = 100
        number_days = 0
        print(f"{self.name}, на нас напали!")
        for i in range(enemy_power):
            if enemy_power > 0:
                enemy_power -= self.power
                number_days += 1
                sleep(1)
                print(f'{self.name} сражается {number_days} день(дня)..., осталось {enemy_power} войнов.')
                if enemy_power <= 0:
                    print(f'{self.name} одержал победу спустя {number_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
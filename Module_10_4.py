from queue import Queue
from random import randint
from threading import Thread
from time import sleep



class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest: Guest | None = None



class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
    def run(self):
        sleep(randint(3,10))

class Cafe:
    def __init__(self, *tables: Table):
        self.tables = list(tables)
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            is_seat = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    is_seat = True
                    guest.start()
                    break
            if not is_seat:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")
    def discuss_guests(self):
        while any(map(lambda x: x.guest, self.tables)) or not self.queue.empty():
            for table in filter(lambda x: x.guest is not None, self.tables):
                table: Table
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"{table.number} стол освободился")
                    table.guest = None
            if not self.queue.empty():
                for table in (table for table in self.tables if table.guest is None):
                    guest = self.queue.get()
                    table.guest = guest
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    guest.start()
                    break

tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


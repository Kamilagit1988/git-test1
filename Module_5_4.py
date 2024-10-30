
class House:
    houses_history = []

    def __new__(cls, *args):
        instance = object.__new__(cls)
        args = args[0]
        cls.houses_history.append(args)
        return instance
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:

            print ('Такого этажа не существует')
        else:
            i = 1
            for i in range(new_floor):
                print(i)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors


    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
            return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
            if isinstance(value, int):
                self.number_of_floors += value
                return self
    def __radd__(self, value):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
            if isinstance(value, int):
                self.number_of_floors += value
                return self





    print(second)
    print(third)


ex = Example('data', second=25, third=3.14)

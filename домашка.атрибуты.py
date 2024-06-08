class House:
    def __init__(self, name, numberfloor):
        self.name = name
        self.numberfloor = numberfloor
    def go_to (self, new_floor):
        if new_floor < 1 or new_floor > self.numberfloor:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

hom = House('ЖК Перспективный', 15)
lift = hom.go_to(int(input('какой этаж:')))


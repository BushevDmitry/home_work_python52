'''Задача №1'''
class NewJournal:

    def set_attr(self,mama, papa, deda, baba):
        self.mama = mama
        self.papa = papa
        self.deda = deda
        self.baba = baba
        self.count_money = self.mama + self.papa + self.deda + self.baba

    def check_money(self):
        if self.count_money < 80:
            print('Денег не хватает')
        else:
            print('Ура, денег хватает!')

masha = NewJournal()
masha.set_attr(10, 20, 30,40)
masha.check_money()


'''Задача №2'''
class Cities:

    def __init__(self):
            self.distance1 = ['Москва','Казань', 838]
            self.distance2 = ['Москва','Самара', 1098]
            self.distance3 = ['Москва','Смоленск', 396]

    def count_distance(self, point1, point2):
        if point1 == point2:
            print(0)
            return

        for distance_cities in [self.distance1, self.distance2, self.distance3]:
            city1, city2, distance = distance_cities

            if (point1 == city1 and point2 == city2) or (point1 == city2 and point2 == city1):
                print(distance)
                break

        else:
            print('Извините, программа ещё в разработке')

city = Cities()
city.count_distance('Москва', 'Казань')
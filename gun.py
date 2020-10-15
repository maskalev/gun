from datetime import datetime
from math import asin, degrees, radians, sin


class GunSettings:
    """Calculation gun settings"""

    def __init__(self):
        self.distance = int(input("Введите расстояние до цели >>> "))
        self.velocity = 1000
        self.g = 9.81

    def angle_calculation(self):
        """Calculation of barrel lift angle"""
        try:
            angle = 90 - degrees((asin(self.distance * self.g /
                                  self.velocity ** 2)) / 2)
            return angle
        except ValueError:
            return "Цель вне зоны поражения."

    def time_calculation(self):
        """Calculation of bullet flight time"""
        alpha = radians(self.angle_calculation())
        time = 2 * self.velocity * sin(alpha) / self.g
        return time

    def add_record(self):
        date = datetime.now().strftime('%d.%m.%y')
        timenow = datetime.now().strftime('%H:%M:%S')
        try:
            angle = round(self.angle_calculation(), 2)
            time = round(self.time_calculation(), 2)
            message = (f"Сегодня {date}. Время {timenow}. Расстояние до цели:"
                       f" {self.distance} м. "
                       f"Угол наклона ствола: {angle} град. "
                       f"Время до взрыва: {time} сек.\n")
        except TypeError:
            message = (f"Сегодня {date}. Время {timenow}. "
                       f"Расстояние до цели: {self.distance} м. Цель вне зоны "
                       f"поражения.\n")
        f = open('topsecret.txt', 'a')
        f.write(message)
        f.close()
        print(f"Запись добавлена.\n{message}")


p = GunSettings()
p.add_record()

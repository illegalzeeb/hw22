# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, field, x_coord, y_coord, direction, is_fly, crawl, speed=1):
        self.field = field
        self.x = x_coord
        self.y = y_coord
        self.is_fly = is_fly
        self.crawl = crawl
        self.direction = direction
        self.speed = speed

    @property
    def speed_calculation(self):
        if self.is_fly and self.crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        elif self.is_fly == True:
            return self.speed * 1.2
        elif self.crawl == True:
            return self.speed * 0.5

    def move(self):
        speed = self.speed_calculation
        if self.direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif self.direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif self.direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif self.direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

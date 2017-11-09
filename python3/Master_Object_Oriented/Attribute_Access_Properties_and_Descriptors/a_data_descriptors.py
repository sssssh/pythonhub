class Unit:
    conversion = 1.0

    def __get__(self, instance, owner):
        return instance.kph * self.conversion

    def __set__(self, instance, value):
        instance.kph = value / self.conversion


class Knots(Unit):
    conversion = 0.5399568


class MPH(Unit):
    conversion = 0.62137119


class KPH(Unit):
    def __get__(self, instance, owner):
        return instance._kph

    def __set__(self, instance, value):
        instance._kph = value


class Measurement:
    kph = KPH()
    knots = Knots()
    mph = MPH()

    def __init__(self, kph=None, mph=None, knots=None):
        if kph:
            self.kph = kph
        elif mph:
            self.mph = mph
        elif knots:
            self.knots = knots
        else:
            raise TypeError

    def __str__(self):
        return "rate: {0.kph} kph = {0.mph} mph = {0.knots} knots".format(self)


if __name__ == "__main__":
    m2 = Measurement(knots=5.9)
    print(m2)
    print("Speed:", m2.mph)

class UnitValue_1:
    """Non-data Descriptor; data local to the descriptor."""
    def __init__(self, unit):
        self.value = None
        self.unit = unit
        self.default_format = "5.2f"

    def __set__(self, instance, value):
        self.value = value

    def __str__(self):
        return "{value:{spec}} {unit}".format(
            spec=self.default_format, **self.__dict__)

    def __format__(self, spec="5.2f"):
        if spec == "":
            spec = self.default_format
        return "{value:{spec}} {unit}".format(spec=spec, **self.__dict__)


class RTD_1:
    rate = UnitValue_1("kt")
    time = UnitValue_1("hr")
    distance = UnitValue_1("nm")

    def __init__(self, rate=None, time=None, distance=None):
        if rate is None:
            self.time = time
            self.distance = distance
            self.rate =distance / time
        if time is None:
            self.rate = rate
            self.distance = distance
            self.rate = distance / time
        if distance is None:
            self.rate = rate
            self.time = time
            self.distance = rate * time

    def __str__(self):
        return "rate: {0.rate} time: {0.time} distance: {0.distance}".format(self)


if __name__ == "__main__":
    m1 = RTD_1(rate=5.8, distance=12)
    print(m1)
    print("Time:", m1.time.value, m1.time.unit)

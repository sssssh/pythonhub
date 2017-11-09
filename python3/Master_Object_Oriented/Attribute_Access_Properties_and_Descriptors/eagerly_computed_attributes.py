class RateTimeDistance(dict):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._solve()

    def __getattribute__(self, name):
        return self.get(name, None)

    def __setattr__(self, name, value):
        self[name] = value
        self._solve()

    def __dir__(self):
        return list(self.keys())

    def _solve(self):
        if self.rate is not None and self.time is not None:
            self['distance'] = self.rate * self.time
        elif self.rate is not None and self.distance is not None:
            self['time'] = self.distance / self.rate
        elif self.time is not None and self.distance is not None:
            self['rate'] = self.distance / self.time


if __name__ == '__main__':
    rtd = RateTimeDistance(rate=6.3, time=8.25, distance=None)
    print("Rate={rate}, Time={time}, Distance={distance}".format(**rtd))

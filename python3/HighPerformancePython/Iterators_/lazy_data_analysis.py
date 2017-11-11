import math
from random import normalvariate, random
from datetime import date, datetime
from itertools import count, groupby, islice, filterfalse, starmap


def read_data(filename):
    with open(filename) as fd:
        for line in fd:
            data = line.strip().split(',')
            yield map(int, data)


def read_fake_data(filename):
    for i in count():
        sigma = random() * 2
        yield (i, normalvariate(0, sigma))


def day_grouper(iterable):
    key_ = lambda timestamp_value: date.fromtimestamp(timestamp_value[0])
    return groupby(iterable, key_)


def check_anomaly(xxx_todo_changme):
    (day, day_data) = xxx_todo_changme
    n = 0
    mean = 0
    M2 = 0
    max_value = None
    for timestamp, value in day_data:
        n += 1
        delta = value - mean
        mean = mean + delta / n
        M2 += delta * (value - mean)
        max_value = max(max_value, value)
    variance = M2 / (n - 1)
    standard_deviation = math.sqrt(variance)

    if max_value > mean + 6 * standard_deviation:
        return day
    return False


def rolling_window_grouper(data, window_size):
    window = tuple(islice(data, 0, window_size))
    while True:
        current_datetime = datetime.fromtimestamp(window[0][0])
        yield (current_datetime, window)
        window = window[1:] + (data.next(),)


if __name__ == "__main__":
    print("Using day_grouper:")
    data = read_fake_data("fake_filename")
    data_day = day_grouper(data)
    print(data_day)
    anomalous_dates = filterfalse(None, starmap(check_anomaly, data_day))
    first_anomalous_date = anomalous_dates.next()
    print("The first anomalous date is: ", first_anomalous_date)
    next_10_dates = islice(anomalous_dates, 10)
    print("The next 10 anomalous dates are: ", list(next_10_dates))

    print("Using rolling_window_grouper:")
    data = read_fake_data("fake_filename")
    data_day = rolling_window_grouper(data, window_size=86400)
    anomalous_dates = filterfalse(None, starmap(check_anomaly, data_day))
    first_anomalous_date = anomalous_dates.next()
    print("The first anomalous date is: ", first_anomalous_date)
    next_10_dates = islice(anomalous_dates, 10)
    print("The next 10 anomalous dates are: ", list(next_10_dates))

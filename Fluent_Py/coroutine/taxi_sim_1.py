import sys
import random
import collections
import queue
import argparse

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 80
SEARCH_DURATION = 4
TRIP_DURATION = 10
DEPARTURE_INTERVAL = 5


Event = collections.namedtuple('Event', 'time proc action')


def compute_delay(interval):
    """Compute action delay using exponential distribution"""
    return int(random.expovariate(1/interval)) + 1


def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        prowling_ends = time + compute_delay(SEARCH_DURATION)
        time = yield Event(prowling_ends, ident, 'pick up passenger')

        trip_ends = time + compute_delay(TRIP_DURATION)
        time = yield Event(trip_ends, ident, 'drop off passenger')
    yield Event(time + 1, ident, 'going home')


class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """Schedule and display events until time is up"""

        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        time = 0
        while time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break

            current_event = self.events.get()
            print('taxi:', current_event.proc,
                  current_event.proc * '   ', current_event)

            time = current_event.time
            proc = self.procs[current_event.proc]
            try:
                next_event = proc.send(time)
            except StopIteration:
                del self.procs[current_event.proc]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
         seed=None):
    """Initialize random generator, build procs and run simulation"""
    if seed is not None:
        random.seed(seed)

    taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)
             for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                        description='Taxi fleet simulator.')
    parser.add_argument('-e', '--end-time', type=int,
                        default=DEFAULT_END_TIME,
                        help='simulation end time; default = %s'
                        % DEFAULT_END_TIME)
    parser.add_argument('-t', '--taxis', type=int,
                        default=DEFAULT_NUMBER_OF_TAXIS,
                        help='number of taxis running; default = %s'
                        % DEFAULT_NUMBER_OF_TAXIS)
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='random generator seed (for testing)')

    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)

from hostage import *

class Strategy(object):
    def __init__(self, number_of_hostages=100):
        self.number_of_hostages = number_of_hostages

    def generate_hostages(self):
        raise NotImplementedError("Use one of the strategy subclasses")


class RandomStrategy(Strategy):
    def generate_hostages(self):
        hostages = [Hostage(i) for i in range(0, self.number_of_hostages-1)]
        random = RandomHostage(self.number_of_hostages-1)
        hostages.append(random)
        return hostages


class CountStrategy(Strategy):
    def generate_hostages(self):
        hostages = [ToggleOnceHostage(i) for i in range(1, self.number_of_hostages)]
        counter = CountHostage(0, self.number_of_hostages)
        hostages.append(counter)
        return hostages


class PeriodStrategy(Strategy):
    def generate_hostages(self):
        hostages = [PeriodHostage(i, self.number_of_hostages, 5) for i in range(0, self.number_of_hostages)]
        return hostages

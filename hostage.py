import random

class Hostage(object):
    def __init__(self, id):
        self.id = id
        self.day = 0
    
    def __repr__(self):
        return 'Hostage(id=%s)' % (self.id)

    def start_new_day(self):
        self.day += 1

    def visit_livingroom(self, light):
        return True    

    def were_all_hostages_in_livingroom(self):
        return False


class CountHostage(Hostage):
    def __init__(self, id, number_of_hostages):
        self.counter = 1
        self.number_of_hostages = number_of_hostages
        super(CountHostage, self).__init__(id)

    def __repr__(self):
        return 'CountHostage(id=%s)' % (self.id)

    def visit_livingroom(self, light):
        if light:
            self.counter += 1
            print "Yet another one!, %s and counting..." % self.counter
        return False

    def were_all_hostages_in_livingroom(self):
        return self.counter >= self.number_of_hostages


class ToggleOnceHostage(Hostage):
    def __init__(self, id):
        self.visited_livingroom = False
        super(ToggleOnceHostage, self).__init__(id)

    def __repr__(self):
        return 'CountHostage(id=%s)' % (self.id)

    def visit_livingroom(self, light):
        if light:
            return True

        if not self.visited_livingroom:
            self.visited_livingroom = True
            print "First time in living room, turn on light"
            return True
        return False


class PeriodHostage(Hostage):
    def __init__(self, id, number_of_hostages, days_in_period):
        self.number_of_hostages = number_of_hostages
        self.memory = [False] * 100
        self.days_in_period = days_in_period
        super(PeriodHostage, self).__init__(id)

    def __repr__(self):
        return 'PeriodHostage(id=%s)' % (self.id)

    def visit_livingroom(self, light):
        self.memory[self.id] = True
        id_of_period = ((self.day - 1) / self.days_in_period) % (self.number_of_hostages - 1)
        if light:
            self.memory[id_of_period] = True
            print "I (%s) know %s has been in the living room, Total: %s" % (self, id_of_period, sum(1 for i in self.memory if i))

        if (self.day - 1) % self.days_in_period == 0:
            return False
        return (self.id == id_of_period)

    def were_all_hostages_in_livingroom(self):
        return sum(1 for i in self.memory if i) == self.number_of_hostages


class RandomHostage(Hostage):
    def __repr__(self):
        return 'RandomHostage(id=%s)' % (self.id)

    def visit_livingroom(self, light):
        return True

    def were_all_hostages_in_livingroom(self):
        return random.choice([True, False, False, False, False, False, False, False, False, False])

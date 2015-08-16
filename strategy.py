from hostage import Hostage, RatHostage

class Strategy(object):
    def generate_hostages(self):
        hostages = [Hostage(i) for i in range(0,99)]
        rat = RatHostage(99)
        hostages.append(rat)
        return hostages

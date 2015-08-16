from livingroom import LivingRoom
from strategy import Strategy
from prison import Prison

from pprint import pprint

strategy = Strategy()
hostages = strategy.generate_hostages()
prison = Prison(hostages)

days = 1
while(not prison.check_if_hostages_must_be_released()):
    days = days + 1


prison_answer = prison.were_all_hostages_in_livingroom()

if not prison_answer:
    print "Your strategy is flawed. Not all hostages have been to the living room, yet a hostage claimed so. All hostages are dead now."
else:
    print "Congrats! The hostages are free after %s days of imprisonment" % days


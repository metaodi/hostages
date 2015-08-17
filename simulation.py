from strategy import *
from prison import Prison
from pprint import pprint

NUMBER_OF_RUNS = 1
NUMBER_OF_HOSTAGES = 100

class FlawedStrategyError(Exception):
    pass


def itersubclasses(cls, _seen=None):
    """
    itersubclasses(cls)
    Generator over all subclasses of a given class, in depth first order.
    """

    if not isinstance(cls, type):
        raise TypeError('itersubclasses must be called with '
                        'new-style classes, not %.100r' % cls)
    if _seen is None:
        _seen = set()
    try:
        subs = cls.__subclasses__()
    except TypeError:  # fails only when cls is type
        subs = cls.__subclasses__(cls)
    for sub in subs:
        if sub not in _seen:
            _seen.add(sub)
            yield sub
            for sub in itersubclasses(sub, _seen):
                yield sub


# iterate over all available strategy classes
strategy_results = {}
for cls in itersubclasses(Strategy):
    strategy = cls(number_of_hostages=NUMBER_OF_HOSTAGES)
    print "##### Strategy: %s #####" % cls.__name__
    strategy_result = {
        'days': [],
        'runs': 0
    }
    for i in range(0, NUMBER_OF_RUNS):
        try:
            hostages = strategy.generate_hostages()
            prison = Prison(hostages, NUMBER_OF_HOSTAGES)
            days = 1

            while(not prison.attempt_to_release_hostages()):
                days = days + 1
            prison_answer = prison.were_all_hostages_in_livingroom()

            if not prison_answer:
                raise FlawedStrategyError("Your strategy is flawed. Not all hostages have been to the living room, yet a hostage claimed so. All hostages are dead now.")
            print "Congrats! The hostages are free after %s days of imprisonment" % days
            strategy_result['days'].append(days)
            strategy_result['runs'] = strategy_result['runs'] + 1
        except FlawedStrategyError, e:
            print str(e)
            continue

    strategy_results[cls.__name__] = strategy_result
    print "##########" 

best_strategy = None
for name, result in strategy_results.iteritems():
    try:
        avg = sum(result['days']) / len(result['days'])
    except ZeroDivisionError:
        avg = "undefined"

    print "##### Strategy: %s, average after %s run(s): %s #####" % (name, result['runs'], avg)
    if best_strategy is None or best_strategy['average'] > avg:
        best_strategy = {
            'name': name,
            'average': avg
        }

print "##########" 
print "##### Best strategy: %s, average %s days of imprisonment" % (best_strategy['name'], best_strategy['average'])

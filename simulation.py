import hostages as h
import argparse

parser = argparse.ArgumentParser(description='Simulate different strategies to solve the classic hostage problem')  # noqa
parser.add_argument('-r', '--runs', help='The number of runs to simulate', type=int, default=1)  # noqa
parser.add_argument('-n', '--hostages', help='The number of hostages to simulate', type=int, default=100)  # noqa
args = parser.parse_args()

# iterate over all available strategy classes
strategy_results = {}
for cls in h.itersubclasses(h.Strategy):
    strategy = cls(number_of_hostages=args.hostages)
    print "##### Strategy: %s #####" % cls.__name__
    strategy_result = {
        'days': [],
        'runs': 0
    }
    for i in range(0, args.runs):
        try:
            hostages = strategy.generate_hostages()
            prison = h.Prison(hostages, args.hostages)
            days = 1

            while(not prison.attempt_to_release_hostages()):
                days = days + 1
            prison_answer = prison.were_all_hostages_in_livingroom()

            if not prison_answer:
                raise h.FlawedStrategyError(
                    "Your strategy is flawed. Not all hostages have been to "
                    "the living room, yet a hostage claimed so. All hostages "
                    "are dead now."
                )
            print (
                "Congrats! The hostages are free after %s days of imprisonment"
                % days
            )
            strategy_result['days'].append(days)
            strategy_result['runs'] = strategy_result['runs'] + 1
        except h.FlawedStrategyError, e:
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

    print (
        "##### Strategy: %s, average after %s run(s): %s #####"
        % (name, result['runs'], avg)
    )
    if best_strategy is None or best_strategy['average'] > avg:
        best_strategy = {
            'name': name,
            'average': avg
        }

print "##########"
print (
    "##### Best strategy: %s, average %s days of imprisonment"
    % (best_strategy['name'], best_strategy['average'])
)

from hostages.livingroom import *  # noqa
from hostages.prison import *  # noqa
from hostages.hostage import *  # noqa
from hostages.strategy import *  # noqa


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

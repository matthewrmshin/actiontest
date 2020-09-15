#!/usr/bin/env python3
"""Classic starter program with a greeting."""


def hello(who: str = 'world') -> str:
    """Return a greeting.

    :param who: Who to greet.
    """
    if who:
        return f'Hello {who}! Hi!'
    else:
        return 'Hello! Hi!'

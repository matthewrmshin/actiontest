#!/usr/bin/env python3
"""CLI for the classic starter program."""

import sys

from hello import hello


def main() -> None:
    """CLI for the classic starter program."""
    try:
        who = sys.argv[1]
    except IndexError:
        print(hello())
    else:
        print(hello(who))
    return

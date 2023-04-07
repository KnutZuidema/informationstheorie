# Read the directory specified by the first argument and return a string of
# the names of all python files in that directory, without the .py extension.
# The names are sorted alphabetically and concatenated together.

import os
import sys


def get_parts(directory):
    parts = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            parts.append(filename[:-3])
    return ''.join(sorted(parts))


if __name__ == "__main__":
    print(get_parts(sys.argv[1]))

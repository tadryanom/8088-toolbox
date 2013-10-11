#!/usr/bin/python

import os

for (root, dirs, files) in os.walk('.'):
    for f in files:
        if f[-1].isupper():
            os.rename(f, f.lower())
    break

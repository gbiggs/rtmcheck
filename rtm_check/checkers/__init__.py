# -*- Python -*-
# -*- coding: utf-8 -*-

'''rtmcheck

Copyright (C) 2009-2014
    Geoffrey Biggs
    Dependable Systems Research Group
    Intelligent Systems Research Institute,
    National Institute of Advanced Industrial Science and Technology (AIST),
    Japan
    All rights reserved.
See LICENSE for licensing details.

Utility to check for potential problems using RT-Middleware.

'''

import os

__all__ = []
for m in os.listdir(os.path.dirname(__file__)):
    if m == '__init__.py' or not m.endswith('.py'):
        continue
    __all__.append(m[:-3])
    __import__(m[:-3], locals(), globals())

del m
del os

# vim: tw=79


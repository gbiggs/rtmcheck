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

Library to check for potential problems using RT-Middleware.

Test checker module 1.

'''

import rtm_check

name = 'Test Check 1'
category = 'Test checkers'
description = 'Place holder description text 1'

def run_check():
    return (rtm_check.PASS, 'This test past')

# vim: tw=79


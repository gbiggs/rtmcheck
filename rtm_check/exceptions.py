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

Exceptions used by the library.

'''

class RTMCheckError(Exception):
    '''Base error class.

    Used for undefined errors that are not core Python errors.

    '''
    pass


class NoSuchCategoryError(RTMCheckError):
    '''Request for a non-existent category.'''
    def __str__(self):
        return 'No such category: {0}'.format(self.args[0])


class NoSuchCheckerError(RTMCheckError):
    '''Request for a non-existent checker.'''
    def __str__(self):
        return 'No such checker: {0}'.format(self.args[0])


# vim: tw=79


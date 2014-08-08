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

Checker manager class responsible for managing available checkers.

'''

import os.path

from rtm_check.exceptions import NoSuchCategoryError, NoSuchCheckerError


class CheckerManager:
    '''Class responsible for managing and running available checkers.

    On construction, all checkers in the rtmchecker.checkers sub-module are
    loaded. Additional checkers may be loaded through the load_from_dir() and
    load_from_file() methods.

    Checker running functions return the results of the executed checkers in a
    dictionary. This dictionary is formatted as below:

    { <category name> :
        { <checker name> : ( [PASS | WARNING | ERROR], <message> ),
          <checker name> : ( [PASS | WARNING | ERROR], <message> ),
          ...
        }
      <category name> :
        { ... },
      ...
    }

    PASS, WARNING and ERROR are constants defined in the checker_base
    sub-module.

    '''

    # self._checkers is a dictionary containing all the loaded checkers.
    # The keys of the dictionary are the categories. Each category is
    # itself a dictionary, where the keys are checker names and the entries
    # are loaded checker modules.

    def __init__(self):
        self._load_default_checkers()

    @property
    def categories(self):
        '''List of all category names available from the loaded checkers.'''
        return self._checkers.keys()

    @property
    def checkers(self):
        '''List of all loaded checkers.

        Format of the list is (<checker>, <category>)'''
        result = []
        for cat in self._checkers:
            result += [(chk, cat) for chk in self._checkers[cat]]
        return result

    def get_checker_description(self, category, checker):
        if category not in self._checkers:
            raise NoSuchCategoryError(category)
        if checker not in self._checkers[category]:
            raise NoSuchCheckerError(c)
        return self._checkers[category][checker].description

    def load_from_dir(self, d):
        '''Load all checkers in the specified directory.'''
        pass

    def load_from_file(self, f):
        '''Load the checker module in the specified file.'''
        pass

    def run_all_checks(self):
        '''Executes all loaded checkers.

        The check results are accumulated in a two-layer hierarchy of
        dictionaries. The first layer is categories, the second layer is
        checkers.
        '''
        results = {}
        for c in self.categories:
            results[c] = self._run_category(self._checkers[c])
        return results

    def run_category_checks(self, categories):
        '''Executes checkers for the specified categories.

        The check results are accumulated in a dictionary keyed by
        '<category>.<checker name>'.
        '''
        results = {}
        for c in categories:
            if c not in self.checkers:
                raise NoSuchCategoryError(c)
            results[c] = self._run_category(c)
        return results

    def run_individual_check(self, category, checker):
        '''Run a single checker.

        The category name and checker name must be provided.
        '''
        if category not in self.checkers:
            raise NoSuchCategoryError(category)
        if checker not in self.checkers[category]:
            raise NoSuchCheckerError(c)
        return {category: {checker:
            self.checkers[category][checker].run_check()}}

    def _run_category(self, category):
        '''Runs all checkers in the provided category dictionary.'''
        results = {}
        for c in category:
            results[c] = category[c].run_check()
        return results

    def _load_default_checkers(self):
        # Finds all checkers in the default locations
        self._checkers = {}
        import rtm_check.checkers
        for checker in [getattr(rtm_check.checkers, m)
                for m in dir(rtm_check.checkers) if not m.startswith('__')]:
            if checker.category not in self._checkers:
                self._checkers[checker.category] = {}
            self._checkers[checker.category][checker.name] = checker

    def _load_checker(self, f):
        # Loads the specified checker module
        pass

# vim: tw=79


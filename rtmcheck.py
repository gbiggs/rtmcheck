#!/usr/bin/env python
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

Main file.

'''

import argparse
import sys

import rtm_check


def print_result(category, checker, result, message):
    if result == rtm_check.PASS:
        res_str = 'PASS'
    elif result == rtm_check.WARNING:
        res_str = 'WARNING'
    else:
        res_str = 'ERROR'
    if message:
        message_str = '\n\t' + message
    else:
        message_str = ''
    print('{res}\t{chk} ({cat}){msg}'.format(res=res_str, cat=category,
        chk=checker, msg=message_str))


def print_results(results, display_all=False):
    for cat in results:
        for check in results[cat]:
            if results[cat][check][0] == rtm_check.PASS and not display_all:
                continue
            print_result(cat, check, results[cat][check][0], results[cat][check][1])


def print_categories(cm):
    for c in cm.categories:
        print(c)


def print_checkers(cm):
    for c in cm.checkers:
        desc = cm.get_checker_description(c[1], c[0])
        print('{chk} ({cat}): {desc}'.format(cat=c[1], chk=c[0], desc=desc))


def main():
    desc = 'Check for problems that may prevent an RT-Middleware ' \
        'application or tool from running correctly.'
    version = 0.1
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-c', '--category', action='append', dest='categories',
        help='Category of checks to execute; if not specified all checks will '
        'be executed')
    parser.add_argument('-e', '--checker', action='append', dest='checkers',
        help='Specific checker to execute. If a category is also given, the ' \
        'checker must be in that category')
    parser.add_argument('--list-categories', action='store_true',
        help='List the available categories')
    parser.add_argument('--list-checkers', action='store_true',
        help='List the available checkers')
    parser.add_argument('-d', '--checker-dir', action='append',
        dest='extra_dirs', help='An additional directory to load checker ' \
        'modules from')
    parser.add_argument('-m', '--checker-module', action='append',
        dest='extra_modules', help='Path to an additional checker module to ' \
        'load')
    parser.add_argument('-a', '--all-results', action='store_true',
            help='Show all results, including successful checks. The ' \
            'default is to only show warnings and errors.')
    args = parser.parse_args()

    cm = rtm_check.checker_manager.CheckerManager()

    if args.extra_dirs:
        for d in args.extra_dirs:
            cm.load_from_dir(d)
    if args.extra_modules:
        for m in args.extra_modules:
            cm.load_from_file(d)

    if args.list_categories:
        # Print a list of categories
        print_categories(cm)
        return 0
    elif args.list_checkers:
        # Print a list of checkers with their descriptions
        print_checkers(cm)
        return 0
    elif args.checkers:
        # Run the specified checkers
        pass
    elif args.categories:
        # Run the specified categories
        results = cm.run_category_checks(args.categories)
    else:
        # Run all checks
        results = cm.run_all_checks()

    print_results(results, args.all_results)


if __name__ == '__main__':
    sys.exit(main())


# vim: tw=79


# todo: you'll need to refactor tests to extract the testing setup which scans the pythonpath for samples see test_captureProperties.py in the pensieve.core.tests module
import fnmatch
import inspect
from functools import partial
import os
from os import getenv
from unittest import TestCase

from os.path import exists, join, isabs, abspath, normpath, relpath

import sys


def with_resources(filepat):
    # todo: work out building a test suite which can take a filename pattern and generate tests for each matching file
    def gen_resource_test(func):
        pass

    #     for resource_path in path_plus:
    #         for path, dirlist, filelist in os.walk(resource_path):
    #             for name in fnmatch.filter(filelist, filepat):
    #                 yield os.path.join(path, name)

    return gen_resource_test


def resourced(fpattern, *args, **kwargs):
    """ accept the name of a file, and decorate a method to use that file in its execution add some arguments
    to the resourced function, including the root, if it exists within the class, and find files matching the
    patterns passed in through the resourced decorator """
    resources = set()
    import re
    fregex = re.compile(fpattern)
    def resource_decorate(func):
        #fixme: I'm currently trying to find the class containing this function, in order to determine if it has a root
        func.resourced = True
        if not func.__name__ == 'setUp':
            raise Exception('resourced is to be raised on the setUp of a TestCase')

        def resourced(*_args, **_kwargs):
            _args[0].resources = set()
            if hasattr(_args[0], 'root') and exists(_args[0].root):
                top = _args[0].root
            else:
                top = os.getcwd()

            # walk the directory structure and determine if resources can be added
            for dirpath, dirnames, filenames in os.walk(top):
                rel = relpath(dirpath, top)
                for name in filenames:
                    if fnmatch.fnmatch(normpath(join(rel, name)), fpattern): # todo: see about cacheing the pattern
                        full_path = join(top, rel, name)
                        _args[0].resources.add(normpath(abspath(full_path)))
            func(*_args, **_kwargs)

        return resourced

    return resource_decorate


def root(directory):
    """ root the function in a resource directory.  If this directory is absolute, then
    the root will be added to the resource_path. Be mindful that a root decorator is intended for use on a class, and
    will find decorators on all of the Class's methods in order to add metadata to them if they are themselves decorated,
    in a manner compliant with this decorator API and if the TestCase plans to use a resource within a root """
    def root_decorate(test_case):
        foo = dir(test_case)
        for name, method in inspect.getmembers(test_case, inspect.ismethoddescriptor):
            if hasattr(method, "resourced"):
                setattr(method, "resources", os.path.join(directory, "foo"))
        root = None
        if isabs(directory) and exists(directory):
            root = abspath(directory)
        else:
            searchpath = getenv("PYTHONPATH").split(';')
            sample_paths = list(filter(exists, map(join, searchpath, (directory for i in range(len(searchpath))))))
            if len(sample_paths) > 0 and exists(sample_paths[0]):
                root = sample_paths[0]
        if not root:
            # todo: figure out how to appropriately raise this exception
            raise Exception("The supplied root {} is not viable".format(directory))
        setattr(test_case, 'root', root)
        return test_case
    return root_decorate


class ResourcefulTestCase(TestCase):
    """ A test conducted using some local resource, if that resource cannot be found on
    the PYTHONPATH, then the test case exists """

    @classmethod
    def setUpClass(cls):
        super(ResourcefulTestCase, cls).setUpClass()
        # build any requisite infrastructure

    @classmethod
    def tearDownClass(cls):
        super(ResourcefulTestCase, cls).setUpClass()
        # tear down any requisite infrastructure

    def setUp(self):
        super().setUp()
        # set up any requisite infrastructure

    def tearDown(self):
        super().tearDown()
        # tear down any requisite infrastructure

class VideoTestCase(ResourcefulTestCase):
    """ A test conducted with the benefit of a sample video """

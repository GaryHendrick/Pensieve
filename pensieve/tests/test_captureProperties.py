# encoding: utf-8
# -----------------------------------------------------------------------------
#  Copyright (c) 2017, Gary Hendrick.
#
#  This file is part of Pensieve.
#
#    Pensieve is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Pensieve is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
#  The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------
""" CaptureProperties is a thin wrapper around the cv2.VideoCapture passed in through its constructor
and """
from functools import partial
from itertools import starmap, chain
from os import walk, listdir, getenv
from os.path import isfile, join, exists, isdir
from unittest import TestCase

import cv2


class TestCaptureProperties(TestCase):
    searchpath = []
    resource_dir = "samples"
    sample_names = ["SampleVideo_176x144_1mb.3gp",
               "SampleVideo_1280x720_1mb.flv",
               "SampleVideo_1280x720_1mb.mkv",
               "SampleVideo_1280x720_1mb.mp4"]
    samples = []

    def find_samples(self):
        self.searchpath = getenv("PYTHONPATH").split(';')
        search_paths = list(filter(isdir, filter(exists, map(join, self.searchpath,
                           (self.resource_dir for i in range(len(self.searchpath)))))))
        samples = [join(path, name) for name in filter(isfile, chain.from_iterable(map(listdir, search_paths)))
                   if name in self.sample_names for path in search_paths]
        for path in search_paths:
            print (path)
            for sample in self.samples:
                join(sample, self.resource_dir)

    def setUp(self):
        self.find_samples()
        self.cap = cv2.VideoCapture()

    def tearDown(self):
        pass

    def test_time(self):
        self.fail()

    def test_time(self):
        self.fail()

    def test_frame(self):
        self.fail()

    def test_frame(self):
        self.fail()

    def test_fcount(self):
        self.fail()

    def test_fcount(self):
        self.fail()

    def test_progress(self):
        self.fail()

    def test_progress(self):
        self.fail()

    def test_width(self):
        self.fail()

    def test_width(self):
        self.fail()

    def test_height(self):
        self.fail()

    def test_height(self):
        self.fail()

    def test_fps(self):
        self.fail()

    def test_fps(self):
        self.fail()

    def test_codec(self):
        self.fail()

    def test_vformat(self):
        self.fail()

    def test_vformat(self):
        self.fail()

    def test_release(self):
        self.fail()

    def test_isOpened(self):
        self.fail()

    def test_read(self):
        self.fail()

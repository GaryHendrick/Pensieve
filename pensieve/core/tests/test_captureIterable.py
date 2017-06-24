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
""" CaptureIterable should be tested solo """
import collections
import inspect
import unittest

import cv2

from pensieve.core.application import CaptureIterable
from pensieve.testing.cases import VideoTestCase, root, resourced


@root('samples')
class TestCaptureIterable(VideoTestCase):
    """ The expectation in this module is to subclass this Iterable for each sample file"""

    def setUp(self):
        if hasattr(self, 'resources'):
            self.video = self.resources.pop()
            self.cap = cv2.VideoCapture(self.video)
            self.iterable = CaptureIterable(self.cap)

    def tearDown(self):
        if hasattr(self, 'cap'): self.cap.release

    def test_iter(self):
        if not hasattr(self, 'iterable'): self.skipTest('no configured iterable in TestCaptureIterable')
        it = iter(self.iterable)
        self.assertIsInstance(it, collections.Iterator)

    def test_next(self):
        if not hasattr(self, 'iterable'): self.skipTest('no configured iterable in TestCaptureIterable')
        it = iter(self.iterable)
        self.assertEqual('GEN_CREATED', inspect.getgeneratorstate(it), 'iterator not in GEN_CREATED state')
        next(it)
        self.assertEqual('GEN_SUSPENDED', inspect.getgeneratorstate(it), 'iterator not in GEN_SUSPENDED state')
        try:
            for x in it: continue
        finally:
            self.assertEqual('GEN_CLOSED', inspect.getgeneratorstate(it), 'iterator not in GEN_CLOSED state')
        self.assertEqual(self.cap.get(cv2.CAP_PROP_FRAME_COUNT), self.cap.get(cv2.CAP_PROP_POS_FRAMES),
                         'frame count is not equal to frame position: iteration check failed on {}'.format(self.video))


class TestIterateMp4(TestCaptureIterable):
    @resourced('SampleVideo_1280x720_1mb.mp4')
    def setUp(self):
        super(TestIterateMp4, self).setUp()


class TestCaptureAgainst3gp(TestCaptureIterable):
    @resourced('SampleVideo_176x144_1mb.3gp')
    def setUp(self):
        super(TestCaptureAgainst3gp, self).setUp()


class TestCaptureAgainstFlv(TestCaptureIterable):
    @resourced('SampleVideo_1280x720_1mb.flv')
    def setUp(self):
        super(TestCaptureAgainstFlv, self).setUp()


class TestCaptureAgainstMkv(TestCaptureIterable):
    @resourced('SampleVideo_1280x720_1mb.mkv')
    def setUp(self):
        super(TestCaptureAgainstMkv, self).setUp()

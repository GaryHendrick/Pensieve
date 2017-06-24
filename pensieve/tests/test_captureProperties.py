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
from os import getenv
from os.path import join, exists

import cv2

from pensieve.cvtools import CaptureProperties
from pensieve.testing.cases import VideoTestCase, resourced


class TestCaptureProperties(VideoTestCase):
    searchpath = []
    resource_dir = "samples"
    sample_names = ["SampleVideo_176x144_1mb.3gp",
                    "SampleVideo_1280x720_1mb.flv",
                    "SampleVideo_1280x720_1mb.mkv",
                    "SampleVideo_1280x720_1mb.mp4"]
    samples = []

    @classmethod
    def find_samples(cls):
        cls.searchpath = getenv("PYTHONPATH").split(';')
        sample_paths = filter(exists, map(join, cls.searchpath, (cls.resource_dir for i in range(len(cls.searchpath)))))
        for spath in sample_paths:
            cls.samples += list(map(partial(join, spath), cls.sample_names))

    @classmethod
    def setUpClass(cls):
        cls.find_samples()

    def setUp(self):
        for sample in iter(self.samples):
            self.cap = cv2.VideoCapture(sample)
            if self.cap.isOpened(): break
        self.sample = sample
        self.props = CaptureProperties(self.cap)

    def tearDown(self):
        self.cap.release()
        del self.props
        del self.cap

    def test_time(self):
        self.assertEqual(self.props.time, 0)

    def test_set_time(self):
        self.assertEqual(self.props.time, 0)
        self.props.time = self.props.length_ms
        self.assertEqual(self.props.time, self.props.length_ms)

    def test_frame(self):
        self.assertEqual(self.props.frame, 0)

    def test_set_frame(self):
        self.props.frame = 10
        self.assertEqual(10, self.props.frame)

    def test_fcount(self):
        self.assertGreater(self.props.fcount, 1)

    def test_progress(self):
        self.assertEqual(0.06666666666666667, self.props.progress)

    def test_set_progress(self):
        self.props.progress = 1.0
        self.assertEqual(self.props.frame, self.props.fcount)

    def test_width(self):
        self.assertEqual(176, self.props.width)

    def test_set_width(self):
        self.props.width = 1280
        self.assertNotEqual(1280, self.props.width)

    def test_height(self):
        self.assertEqual(144, self.props.height)

    def test_set_height(self):
        self.props.height = 720
        self.assertNotEqual(720, self.props.height)

    def test_fps(self):
        self.assertEqual(15, self.props.fps)

    def test_set_fps(self):
        self.props.fps = 24
        self.assertTrue(24, self.props.fps)

    def test_codec(self):
        """ This test will currently fail.  See the CaptureProperties.codec comments for details"""
        self.assertEqual(0, self.props.codec)

    def test_vformat(self):
        self.assertEqual(0, self.props.vformat)

    def test_release(self):
        self.assertTrue(self.props.isOpened())
        self.props.release()
        self.assertFalse(self.props.isOpened())

    def test_isOpened(self):
        self.assertTrue(self.props.isOpened())

    def test_read(self):
        res, frame = self.props.read()
        self.assertTrue(res)

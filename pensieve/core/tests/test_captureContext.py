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
""" unit testing for CaptureContext """

from unittest import TestCase

import cv2

from pensieve.core.application import CaptureContext


class TestCaptureContext(TestCase):
    matcount = 100

    def test_camera_iteration_context(self):
        context = CaptureContext(0)
        with context as capturable:
            i = 0
            self.assertTrue(context._cap.isOpened())
            self.assertTrue(context._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            for mat in capturable:
                self.assertTrue(mat.any())
                i +=1
                if i == 100: break
        self.assertFalse(context._cap.isOpened())

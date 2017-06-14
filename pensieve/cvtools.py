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
""" cvtools provides a number of useful open cv support tools """
import cv2


class CaptureProperties(object):
    """  video props from http://docs.opencv.org/3.2.0/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704da7c2fa550ba270713fca1405397b90ae0
    and http://docs.opencv.org/3.0-beta/modules/videoio/doc/reading_and_writing_video.html#videocapture-get
    """

    def __init__(self, capture: cv2.VideoCapture):
        super(CaptureProperties, self).__init__()

        self._cap = capture
        self._fcount = 0

    @property
    def time(self):
        return self._cap.get(cv2.CAP_PROP_POS_MSEC)

    @time.setter
    def time(self, value):
        if value > self.length_ms:
            raise ValueError('value must be < {self.length_ms}')
        else:
            self._cap.set(cv2.CAP_PROP_POS_MSEC, value)

    @property
    def frame(self):
        return int(self._cap.get(cv2.CAP_PROP_POS_FRAMES))

    @frame.setter
    def frame(self, value):
        if (0 > value or (0 < self.fcount and value > self.fcount)):
            raise ValueError('value must be > 0 and < {self.fcount}'.format(self=self))

        self._cap.set(cv2.CAP_PROP_POS_FRAMES, value)

    @property
    def fcount(self):
        if self._cap.get(cv2.CAP_PROP_FRAME_COUNT) < 0:
            return self._fcount
        else:
            return self._cap.get(cv2.CAP_PROP_FRAME_COUNT)

    @fcount.setter
    def fcount(self, value):
        if self._cap.get(cv2.CAP_PROP_FRAME_COUNT) < 0:
            self._fcount = value
        else:
            self._cap.set(cv2.CAP_PROP_FRAME_COUNT, value)

    @property
    def progress(self):
        result = self._cap.get(cv2.CAP_PROP_POS_AVI_RATIO)
        if self.fcount == 0: return result
        if result < 1.0 / self.fcount:
            return 0.0
        else:
            return result

    @progress.setter
    def progress(self, value):
        if value < 0.0 or value > 1.0:
            raise ValueError("value must be between 0.0 and 1.0")
        else:
            self._cap.set(cv2.CAP_PROP_POS_AVI_RATIO, value)

    @property
    def width(self):
        return int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    @width.setter
    def width(self, value):
        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, value)

    @property
    def height(self):
        return int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    @height.setter
    def height(self, value):
        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, value)

    @property
    def fps(self):
        return int(self._cap.get(cv2.CAP_PROP_FPS))

    @fps.setter
    def fps(self, value):
        self._cap.set(cv2.CAP_PROP_FPS, value)

    @property
    def codec(self):
        return self._cap.get(cv2.CAP_PROP_FOURCC)

    @property
    def vformat(self):
        return self._cap.get(cv2.CAP_PROP_FORMAT)

    @vformat.setter
    def vformat(self, value):
        return self._cap.set(cv2.CAP_PROP_FORMAT, value)

    def __repr__(self):
        return "{self.__class__.__name__}({self.width}x{self.height}@{self.fps}fps in {self.codec} in {self.vformat})".format(
            self=self)

    def release(self):
        self._cap.release()

    def isOpened(self):
        return self._cap.isOpened()

    def read(self):
        return self._cap.read()

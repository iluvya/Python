#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script shakes cursor until the button is pressed
"""

from ctypes import byref, c_long, Structure, windll
import random
import time
import threading

_STOP = False


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def shake_cursor_windows():
    """
    Move windows cursor
    """
    while True:
        if _STOP:
            break
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        windll.user32.SetCursorPos(pt.x + random.choice([-2, -1, 0, 1, 2]),
                                   pt.y + random.choice([-2, -1, 0, 1, 2]))
        time.sleep(0.01)


def main():
    global _STOP
    x = threading.Thread(target=shake_cursor_windows)
    x.start()
    response = windll.user32.MessageBoxW(0, "Hello!", "Python says:", 0)
    if response == 1:
        _STOP = True
    x.join()


if __name__ == '__main__':
    main()

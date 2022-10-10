#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script binds keyboard shortcuts 
to enable/disable mouse auto click at time interval.
"""

import keyboard, mouse
import time
from threading import Thread

clicking = False
done = False
click_interval = 30


def click(click_interval):
    """
    Mouse left button click at time interval.
    """
    global done
    global clicking
    clicking = True
    while not done:
        if clicking:
            mouse.click()
            time.sleep(click_interval)


def _start():
    clicker_thread = Thread(target=click, args=(click_interval,))
    clicker_thread.start()


def _stop():
    global clicking
    clicking = False


def _quit():
    global done
    done = True

   
def set_shortcuts():
    keyboard.add_hotkey('ctrl+alt+e', _start)
    keyboard.add_hotkey('ctrl+alt+c', _stop)
    keyboard.add_hotkey('ctrl+alt+q', _quit)


def main():
    global done
    set_shortcuts()
    print('Ctrl + Alt + E to start clicking')
    print('Ctrl + Alt + C to stop clicking')
    print('Ctrl + Alt + Q to quit')
    while not done:
        time.sleep(0.1)

 
if __name__ == '__main__':
    main()

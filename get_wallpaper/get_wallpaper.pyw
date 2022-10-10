#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script downloads and sets a random wallpaper
"""

import json
import os
from ctypes import windll

import requests
from PIL import Image

_path_home = os.environ['USERPROFILE']
_wallpaper_name = 'wallpaper.jpg'
_wallpaper_path = os.path.join(_path_home, _wallpaper_name)

_URL = "https://wallhaven.cc/api/v1/search"
_query = '+gradient +texture +minimalism'
_categories = '100'
_purity = '100'
_resolutions = '1920x1080'
_sorting = 'random'
_order = 'desc'


def set_wallpaper_windows(wallpaper_path):
    """
    Call winapi function to set a wallpaper
    """
    SPI_SETDESKWALLPAPER = 0x14
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02
    windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,
                                        0,
                                        wallpaper_path,
                                        SPIF_SENDWININICHANGE
                                        | SPIF_UPDATEINIFILE)


def main ( ):
    PARAMS = {'q':           _query,
              'categories':  _categories,
              'purity':      _purity,
              'resolutions': _resolutions,
              'sorting':     _sorting,
              'order':       _order}

    response = requests.get(url=_URL, params=PARAMS)
    data = response.json()
    image_path = data['data'][0]['path']
    image_type = data['data'][0]['file_type']
    response = requests.get(url=image_path)
    open(_wallpaper_path,'wb').write(response.content)
    if 'image/png' == image_type:
        # Convert to jpg
        im = Image.open(_wallpaper_path).convert('RGB').save(_wallpaper_path)
    set_wallpaper_windows(_wallpaper_path)


if __name__ == '__main__':
    main()

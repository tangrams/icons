#!/usr/bin/env python

# THIS IS NOT A GENERAL PURPOSE TOOL, YET. NO.
# STOP THINKING IT IS. YOU WILL ONLY BE SAD.
# (20160323/thisisaaronland)

import requests
import yaml
import re
import sys
import os

import cStringIO
from PIL import Image

pat = re.compile('([^\:]+)\:\s+\[(\d+),\s+(\d+),\s+(\d+),\s+(\d+)\]')

if __name__ == '__main__':

    root = "https://raw.githubusercontent.com/tangrams/refill-style/gh-pages/"

    src_yaml = root + "refill-style.yaml"
    rsp = requests.get(src_yaml)

    """
    data = yaml.safe_load(rsp.content)
    print data
    sys.exit()
    """

    textures = False
    pois = False
    sprites = False

    lookup = {}
    url = None

    for ln in rsp.content.split("\n"):

        ln = ln.strip()

        if ln.startswith("#"):
            continue

        if ln == 'textures:':
            textures = True

        if not textures:
            continue

        if ln == 'pois:':
            pois = True

        if not pois:
            continue

        if ln.startswith('url:'):

            ignore, url = ln.split(': ')

        if ln == 'sprites:':
            sprites = True

        if not sprites:
            continue

        if ln == '':
            break

        m = pat.match(ln)

        if not m:
            continue

        g = m.groups()

        name = g[0]
        dims = map(int, g[1:])

        lookup[name] = dims

    # print lookup

    src_icons = root + url
    rsp = requests.get(src_icons)

    fh = cStringIO.StringIO(rsp.content)
    img = Image.open(fh)

    for name, dims in lookup.items():
        
        fname = "%s.png" % name
        path = os.path.join("icons", fname)

        x1, y1, x2, y2 = dims
        x2 = x1 + x2
        y2 = y1 + y2

        i = img.crop((x1, y1, x2, y2))
        i.save(path)

        print path

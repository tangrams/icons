#!/usr/bin/env python

import sys
import os
import logging

import requests
import yaml
import json
import re

import cStringIO
from PIL import Image

pat = re.compile('([^\:]+)\:\s+\[(\d+),\s+(\d+),\s+(\d+),\s+(\d+)\]')

def extract_icons(style):

    src_yaml = "https://raw.githubusercontent.com/tangrams/%s/gh-pages/%s.yaml" % (style, style)
    rsp = requests.get(src_yaml)

    # See notes and comments in here. Parsers, yeah?
    # https://github.com/whosonfirst/whosonfirst-www-boundaryissues/issues/73
    # (20160323/thisisaaronland)

    """
    data = yaml.safe_load(rsp.content)
    print data
    sys.exit()
    """

    textures = False
    pois = False
    sprites = False

    icons = {}
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

        icons[name] = dims

    return icons, url

if __name__ == '__main__':

    import optparse
    opt_parser = optparse.OptionParser()

    opt_parser.add_option('-s', '--style', dest='style', action='store', default=None, help='Which style to extract icons for')
    opt_parser.add_option('-o', '--outdir', dest='outdir', action='store', default=None, help='Where to save the extracted icons (default is the current working directory)')

    opt_parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Be chatty (default is false)')
    options, args = opt_parser.parse_args()

    if options.verbose:	
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if not options.style:
        logging.error("You forgot to specify a style")
        sys.exit(1)

    style = options.style
    outdir = options.outdir

    try:
        icons, url = extract_icons(style)
    except Exception, e:
        logging.error("failed to extract icons for %s, because %s" % (style, e))
        sys.exit(1)

    if not outdir:
        outdir = os.getcwd()

    outdir = os.path.abspath(outdir)
    outdir = os.path.join(outdir, style)

    logging.info("writing %s icons to %s" % (style, outdir))

    if not os.path.exists(outdir):
        logging.debug("creating %s" % outdir)
        os.makedirs(outdir)

    src_icons = "https://raw.githubusercontent.com/tangrams/%s/gh-pages/%s" % (style, url)
    rsp = requests.get(src_icons)

    fh = cStringIO.StringIO(rsp.content)
    img = Image.open(fh)

    index = {}

    for name, dims in icons.items():
        
        fname = "%s.png" % name
        path = os.path.join(outdir, fname)

        x1, y1, x2, y2 = dims
        x2 = x1 + x2
        y2 = y1 + y2

        logging.info("save %s to %s" % (name, path))
        i = img.crop((x1, y1, x2, y2))

        index[ name ] = { 'width': i.width, 'height': i.height }
        i.save(path)

    path_index = os.path.join(outdir, "index.json")
    fh = open(path_index, "w")

    json.dump(index, fh, indent=2)
    fh.close()

    # TO DO: purge icons in outdir that are not in index?
    
    sys.exit(0)

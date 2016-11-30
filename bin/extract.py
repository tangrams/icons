#!/usr/bin/env python

import sys
import os
import logging

import requests
import yaml
import json
import re

import cStringIO

try:
    from PIL import Image as _imaging
except ImportError:
    from PIL.Image import core as _imaging

pat = re.compile('([^\:]+)\:\s+\[(\d+),\s+(\d+),\s+(\d+),\s+(\d+)\]')

def extract_sprites(style, local, resolution):
    if local:
        src_yaml = "spritesheet/%s@%sx.yaml" % (style, resolution)
        # note, Mac new lines, omg
        f = open(src_yaml, 'rU')
        yaml = f.read()
        f.close()
    else:
        if style == "bubble-wrap":
            src_yaml = "https://mapzen.com/carto/%s-style/%s.yaml"  % (style, style)
        else:
            src_yaml = "https://mapzen.com/carto/%s-style/%s-style.yaml"  % (style, style)
        rsp = requests.get(src_yaml)
        yaml = rsp.content

    print yaml

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

    sprite = {}
    url = None

    for ln in yaml.split("\n"):

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

        sprite[name] = dims

    return sprite, url

if __name__ == '__main__':

    import optparse
    opt_parser = optparse.OptionParser()

    opt_parser.add_option('-s', '--style', dest='style', action='store', default=None, help='Which style to extract sprites for')
    opt_parser.add_option('-l', '--local', dest='local', action='store_true', default=False, help='Local or remote style')
    opt_parser.add_option('-r', '--resolution', dest='resolution', action='store', default=2, help='Resolution (eg: 1, 2, 3, 4, 8)')
    opt_parser.add_option('-o', '--outdir', dest='outdir', action='store', default=None, help='Where to save the extracted sprites (default is the current working directory)')

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
    local = options.local
    resolution = str(options.resolution)
    outdir = options.outdir

    try:
        sprites, spritesheet = extract_sprites(style, local, resolution)
    except Exception, e:
        logging.error("failed to extract sprites for %s, because %s" % (style, e))
        sys.exit(1)

    #print sprites
    #print spritesheet

    if not outdir:
        outdir = os.getcwd()

    outdir = os.path.abspath(outdir)
    outdir = os.path.join(outdir, style + "-style")
    outdir = os.path.join(outdir, resolution + "x")

    logging.info("writing %s sprites to %s" % (style, outdir))

    if not os.path.exists(outdir):
        logging.debug("creating %s" % outdir)
        os.makedirs(outdir)

    if local:
        src_spritesheet = "spritesheet/%s@%sx.png" % (style, resolution)
        fh_spritesheet = open(src_spritesheet, 'r')

        img = _imaging.open(fh_spritesheet)
    else:
        if style == "bubble-wrap":
            src_spritesheet = "https://mapzen.com/carto/%s-style/%s"  % (style, spritesheet)
        else:
            src_spritesheet = "https://mapzen.com/carto/%s-style/%s"  % (style, spritesheet)
        rsp = requests.get(src_spritesheet)

        fh = cStringIO.StringIO(rsp.content)
        img = _imaging.open(fh)

    index = {}

    for name, dims in sprites.items():

        fname = "%s.png" % name
        path = os.path.join(outdir, fname)

        x1, y1, x2, y2 = dims
        x2 = x1 + x2
        y2 = y1 + y2

        logging.info("save %s to %s" % (name, path))
        i = img.crop((x1, y1, x2, y2))

        try:
            index[ name ] = { 'width': i.width, 'height': i.height }
        except:
            index[ name ] = { 'width': i.size[0], 'height': i.size[1] }

        i.save(path)

    path_index = os.path.join(outdir, "index.json")
    fh = open(path_index, "w")

    json.dump(index, fh, indent=2)
    fh.close()

    # TO DO: purge icons in outdir that are not in index?

    sys.exit(0)

# icons

WIP: The source Illustrator files for [color](POI_Icons-mod23.ai) and [b&w](POI_Icons-mod23-bw.ai) icons used in
Eraser Map, Refill, Zinc, and Cinnabar house Mapzen styles.

Binary files are hard to version and collaborate around in Github,
so please be gentle and checkin with @sensescape and @nvkelso
before making changes.

The [JSX script](ai-spritesheet-factory_mapzen_v2.jsx) is run from within Illustrator to export the spritesheet
image file and CSS with the texture definitions.

The [YML file](ai-spritesheet-factory-config.yml) is the config file for the JSX script.

Output goes into the [build](build/) dir.

After spritesheet generation, the [PY script](pngpixelbleed.py) needs to be run to pre-blend pixels so
PNG24 format images don't have dirty pixels on the transparency collar in Tangram.

![icon-preview](https://raw.githubusercontent.com/tangrams/icons/master/build/poi_icons_18%402x.png)

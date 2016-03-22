# icons

The source Illustrator files for color and b&w icons used in 
Eraser Map, Refill, Zinc, and Cinnabar house Mapzen styles.

Binary files are hard to version and collaborate around in Github, 
so please be gentle and checkin with @sensescape and @nvkelso 
before making changes.

The JSX script is run from within Illustrator to export the spritesheet
image file and CSS with the texture definitions. 

The YML file is the config file for the JSX script.

After spritesheet generation, the PY script needs to be run to pre-blend pixels so 
PNG24 format images don't have dirty pixels on the transparency collar in Tangram.

This repo is meant to be private for now. Eventually we'll open this all up...

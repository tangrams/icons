all: refill bubble-wrap walkabout tron

clean:
	rm -rf sprite

refill: refill-dirty-pixels
	./bin/extract.py -s refill -l -r 1 -o ./sprite
	./bin/extract.py -s refill -l -r 2 -o ./sprite
	./bin/extract.py -s refill -l -r 3 -o ./sprite
	./bin/extract.py -s refill -l -r 4 -o ./sprite
	./bin/extract.py -s refill -l -r 8 -o ./sprite
	./bin/extract.py -s refill -l -r 16 -o ./sprite

bubble-wrap: bubble-wrap-dirty-pixels
	./bin/extract.py -s bubble-wrap -l -r 1 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 2 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 3 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 4 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 8 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 16 -o ./sprite

bubble-wrap-shields-usa: bubble-wrap-shields-usa-dirty-pixels
	./bin/extract.py -s bubble-wrap-shields-usa -l -r 1 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-usa -l -r 2 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-usa -l -r 3 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-usa -l -r 4 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-usa -l -r 8 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-usa -l -r 16 -o ./sprite

bubble-wrap-shields-international: bubble-wrap-shields-international-dirty-pixels
	./bin/extract.py -s bubble-wrap-shields-international -l -r 1 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-international -l -r 2 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-international -l -r 3 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-international -l -r 4 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-international -l -r 8 -o ./sprite
	./bin/extract.py -s bubble-wrap-shields-international -l -r 16 -o ./sprite

walkabout: walkabout-dirty-pixels
	./bin/extract.py -s walkabout -l -r 1 -o ./sprite
	./bin/extract.py -s walkabout -l -r 2 -o ./sprite
	./bin/extract.py -s walkabout -l -r 3 -o ./sprite
	./bin/extract.py -s walkabout -l -r 4 -o ./sprite
	./bin/extract.py -s walkabout -l -r 8 -o ./sprite
	./bin/extract.py -s walkabout -l -r 16 -o ./sprite

tron: tron-wrap-dirty-pixels
	./bin/extract.py -s tron -l -r 1 -o ./sprite
	./bin/extract.py -s tron -l -r 2 -o ./sprite
	./bin/extract.py -s tron -l -r 3 -o ./sprite
	./bin/extract.py -s tron -l -r 4 -o ./sprite
	./bin/extract.py -s tron -l -r 8 -o ./sprite
	./bin/extract.py -s tron -l -r 16 -o ./sprite

refill-dirty-pixels:
	python ./bin/pngpixelbleed.py spritesheet/refill@1x.png
	python ./bin/pngpixelbleed.py spritesheet/refill@2x.png
	python ./bin/pngpixelbleed.py spritesheet/refill@3x.png
	python ./bin/pngpixelbleed.py spritesheet/refill@4x.png
	python ./bin/pngpixelbleed.py spritesheet/refill@8x.png
	python ./bin/pngpixelbleed.py spritesheet/refill@16x.png

bubble-wrap-dirty-pixels:
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap@1x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap@2x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap@3x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap@4x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap@8x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap@16x.png

bubble-wrap-shields-usa-dirty-pixels:
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-usa@1x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-usa@2x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-usa@3x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-usa@4x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-usa@8x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-usa@16x.png

bubble-wrap-shields-international-dirty-pixels:
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-international@1x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-international@2x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-international@3x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-international@4x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-international@8x.png
	python ./bin/pngpixelbleed.py spritesheet/bubble-wrap-shields-international@16x.png

walkabout-dirty-pixels:
	python ./bin/pngpixelbleed.py spritesheet/walkabout@1x.png
	python ./bin/pngpixelbleed.py spritesheet/walkabout@2x.png
	python ./bin/pngpixelbleed.py spritesheet/walkabout@3x.png
	python ./bin/pngpixelbleed.py spritesheet/walkabout@4x.png
	python ./bin/pngpixelbleed.py spritesheet/walkabout@8x.png
	python ./bin/pngpixelbleed.py spritesheet/walkabout@16x.png

tron-wrap-dirty-pixels:
	python ./bin/pngpixelbleed.py spritesheet/tron@1x.png
	python ./bin/pngpixelbleed.py spritesheet/tron@2x.png
	python ./bin/pngpixelbleed.py spritesheet/tron@3x.png
	python ./bin/pngpixelbleed.py spritesheet/tron@4x.png
	python ./bin/pngpixelbleed.py spritesheet/tron@8x.png
	python ./bin/pngpixelbleed.py spritesheet/tron@16x.png

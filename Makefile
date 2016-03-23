pngs: refill-pngs erasermap-pngs

refill-pngs:
	./bin/extract.py -s refill-style -o ./png

erasermap-pngs:
	./bin/extract.py -s eraser-map -o ./png
	
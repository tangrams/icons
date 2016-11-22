pngs: refill-sprites bubble-wrap-sprites walkabout-sprites

refill-sprites:
	./bin/extract.py -s refill -o ./sprite

bubble-wrap-sprites:
	./bin/extract.py -s bubble-wrap -o ./sprite

walkabout-sprites:
	./bin/extract.py -s walkabout -o ./sprite

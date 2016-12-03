all: refill bubble-wrap walkabout tron

clean:
	rm -rf sprite

refill:
	./bin/extract.py -s refill -l -r 1 -o ./sprite
	./bin/extract.py -s refill -l -r 2 -o ./sprite
	./bin/extract.py -s refill -l -r 3 -o ./sprite
	./bin/extract.py -s refill -l -r 4 -o ./sprite
	./bin/extract.py -s refill -l -r 8 -o ./sprite
	./bin/extract.py -s refill -l -r 16 -o ./sprite

bubble-wrap:
	./bin/extract.py -s bubble-wrap -l -r 1 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 2 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 3 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 4 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 8 -o ./sprite
	./bin/extract.py -s bubble-wrap -l -r 16 -o ./sprite

walkabout:
	./bin/extract.py -s walkabout -l -r 1 -o ./sprite
	./bin/extract.py -s walkabout -l -r 2 -o ./sprite
	./bin/extract.py -s walkabout -l -r 3 -o ./sprite
	./bin/extract.py -s walkabout -l -r 4 -o ./sprite
	./bin/extract.py -s walkabout -l -r 8 -o ./sprite
	./bin/extract.py -s walkabout -l -r 16 -o ./sprite

tron:
	./bin/extract.py -s tron -l -r 1 -o ./sprite
	./bin/extract.py -s tron -l -r 2 -o ./sprite
	./bin/extract.py -s tron -l -r 3 -o ./sprite
	./bin/extract.py -s tron -l -r 4 -o ./sprite
	./bin/extract.py -s tron -l -r 8 -o ./sprite
	./bin/extract.py -s tron -l -r 16 -o ./sprite

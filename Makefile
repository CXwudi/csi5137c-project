init:
	pip3 install -r src/requirements.txt

test:
	python3 -m unittest discover -s "src" -p "*_test.py"
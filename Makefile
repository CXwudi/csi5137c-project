init:
	pip3 install -r src/main/requirements.txt

test:
	python3 -m unittest discover -s "src/test" -p "*.py"
deps2:
	pip install --user -r requirements.txt

localrun:
	python -m uvicorn routes:app

deps:
	pip3 install -r requirements.txt

winrun:
	python -m uvicorn routes:app --host 0.0.0.0

winrun2:
	python -m uvicorn routes:app --host 127.0.0.1

run:
	uvicorn routes:app --host 0.0.0.0

dev:
	uvicorn routes:app --reload

error:
	python -m uvicorn routes:app --reload
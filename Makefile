unit-test:
	cd programs && PYTHONPATH=${PYTHONPATH}:${PWD} nosetests tests

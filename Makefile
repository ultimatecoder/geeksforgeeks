unit-test:
	cd programs && PYTHONPATH=${PYTHONPATH}:${PWD} nosetests tests
end-to-end-test:
	garud end_to_end_tests

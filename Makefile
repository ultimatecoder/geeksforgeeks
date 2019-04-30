unit-test:
	cd programs && PYTHONPATH=${PYTHONPATH}:${PWD} nosetests tests
end-to-end-test:
	PYTHONPATH=${PYTHONPATH}:${PWD}/programs PATH=${PATH}$(shell find ${PWD}/programs -type d -printf ":%p") cucumber
build-dev:
	bundle install

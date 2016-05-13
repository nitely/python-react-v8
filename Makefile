clean:
	rm -fr dist/ doc/_build/

docs:
	cd docs && make clean && make html

test:
	python runtests.py

build-examples:
	export NODE_ENV=production
	cd examples/flux && npm install && npm run bundle
	cd examples/simple && npm install && npm run bundle
	python build_examples.py

sdist: test clean
	python setup.py sdist

release: test clean
	python setup.py sdist upload

.PHONY: clean docs test build-examples sdist release

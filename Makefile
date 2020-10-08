.PHONY: init shell rm manifest clean-build clean reinit

init:
	export PIPENV_VENV_IN_PROJECT=1 && \
	pipenv install --python 3.6 --dev

shell:
	pipenv shell

rm:
	pipenv --rm

manifest:
	pipenv run check-manifest --verbose --create --update

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean: clean-build

reinit: rm init

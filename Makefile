.PHONY: init shell rm manifest

init:
	export PIPENV_VENV_IN_PROJECT=1 && \
	pipenv install --python 3.6 --dev

shell:
	pipenv shell

rm:
	pipenv --rm

manifest:
	pipenv run check-manifest --verbose --create --update

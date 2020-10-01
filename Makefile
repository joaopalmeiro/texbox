.PHONY: init shell remove manifest

init:
	export PIPENV_VENV_IN_PROJECT=1 && \
	pipenv install --python 3.6 --dev

shell:
	pipenv shell

remove:
	pipenv --rm

manifest:
	pipenv run check-manifest --verbose --create --update

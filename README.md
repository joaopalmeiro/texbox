# texbox

[![PyPI - Version](https://img.shields.io/pypi/v/texbox)](https://pypi.org/project/texbox/)
![Publish to PyPI](https://github.com/joaopalmeiro/texbox/workflows/Publish%20to%20PyPI/badge.svg)

A Python CLI to organize and prettify specific .tex files.

## Quickstart (CLI)

```text
usage: texbox [-h] -i PATH [-b {label,abbrv,full}] [-d]

Sort acronyms from an `acronyms.tex` file.

required arguments:
  -i, --input PATH      The path to the `acronyms.tex` file to be sorted.

optional arguments:
  -b, --by {label,abbrv,full}
                        Macro argument name to sort by. (default: label)
  -d, --descending      Sort descending instead of ascending.
```

## Development quickstart

- `make init`.
- `make shell` or `pipenv shell`.

## References

- [LaTeX/Glossary](https://en.wikibooks.org/wiki/LaTeX/Glossary).
- [Publishing package distribution releases using GitHub Actions CI/CD workflows](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/).

## Notes

- `pipenv install --python 3.6 --dev`.
- `pipenv install -e .`.
- `pipenv install pyparsing`.
- `pipenv graph`.
- Delete tag: `git push --delete origin tagname`.

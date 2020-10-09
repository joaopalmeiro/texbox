# texbox

[![PyPI - Version](https://img.shields.io/pypi/v/texbox)](https://pypi.org/project/texbox/)
![Publish to PyPI](https://github.com/joaopalmeiro/texbox/workflows/Publish%20to%20PyPI/badge.svg)

A Python CLI to organize and prettify specific .tex files.

## Quickstart (CLI)

### texbox_acronyms

```text
usage: texbox_acronyms [-h] -i PATH [-b {label,abbrv,full}] [-d]

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
- [The Comprehensive LaTeX Symbol List](https://math.uoregon.edu/wp-content/uploads/2014/12/compsymb-1qyb3zd.pdf).

## Notes

- `pipenv install --python 3.6 --dev`.
- `pipenv install -e .`.
- `pipenv install pyparsing`.
- `pipenv graph`.
- Delete tag: `git push --delete origin tagname`.
- `python -m texbox.cli_acronyms -h`.
- [`pandas.DataFrame.to_latex`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_latex.html) documentation.
- `texbox_tables -i literature_review_summary.csv -ck "Cite Key" -o table1.tex -t "Paper" -c "Granularity"`.

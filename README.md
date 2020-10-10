# texbox

[![PyPI - Version](https://img.shields.io/pypi/v/texbox)](https://pypi.org/project/texbox/)
![Publish to PyPI](https://github.com/joaopalmeiro/texbox/workflows/Publish%20to%20PyPI/badge.svg)

An opinionated Python CLI to create, organize, and prettify specific files of a LaTeX project.

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

### texbox_tables

```text
usage: texbox_tables [-h] -i PATH -o PATH -ck COL -t COL [-c COLS] [-a COLS]
                     [-r] [-b] [-ca STR] [-sb COLS] [-fl PATH]

Generate a LaTeX table from a bibliography-based file.

required arguments:
  -i, --input PATH      The path to the file to be tabulated.
  -o, --output PATH     The path to the file for the generated LaTeX table.
  -ck, --cite-key-col COL
                        The column name for the cite key.
  -t, --title-col COL   The column name for the title.

optional arguments:
  -c, --cols COLS       The subset of columns to maintain. By default, all
                        columns are kept except the title column.
  -a, --acronym-cols COLS
                        The subset of columns whose name is an acronym and
                        which must be wrapped in a macro. By default, no
                        column name is considered an acronym.
  -r, --rotate          Rotate the generated LaTeX table (landscape mode).
  -b, --break-column-headings
                        Break the column headings of the generated LaTeX table
                        with more than one word.
  -ca, --caption STR    The caption for the generated LaTeX table.
  -sb, --sort-by COLS   The subset of columns to sort by.
  -fl, --footer-legend PATH
                        The path to the file with the footer legend entries.
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
- `texbox_tables -i literature_review_summary.csv -ck "Cite Key" -o table1.tex -t "Paper" -c "Year,OOTL,BC,MCC,Other Tasks,uFeatures,Multiple Models,Tracking of Changes,OOTB,Context,Target Group,Model,OSS" -a "OOTL,BC,MCC,uFeatures,OOTB,OSS" -r -b -ca "Summary of visual tools for Model Evaluation." -sb "Year" -fl literature_review_summary_footer.txt`.
- `texbox_tables -i literature_review_summary.csv -ck "Cite Key" -o table1.tex -t "Paper" -c "Year,Granularity" -ca "Summary of granularities of visual tools for Model Evaluation." -sb "Year"`.

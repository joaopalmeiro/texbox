import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


def get_version(root, rel_path):
    for line in (root / rel_path).read_text().splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find the version string (`__version__`).")


setup(
    name="texbox",
    version=get_version(HERE, "texbox/__init__.py"),
    description="An opinionated Python CLI to create, organize, and prettify specific files of a LaTeX project.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="João Palmeiro",
    author_email="jm.palmeiro@campus.fct.unl.pt",
    url="https://github.com/joaopalmeiro/texbox",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Terminals",
        "Topic :: Text Processing :: Markup :: LaTeX",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    license="MIT",
    keywords="cli, refactor, sort, prettify, acronyms, latex",
    install_requires=["pyparsing", "pandas"],
    entry_points={
        "console_scripts": [
            "texbox_acronyms=texbox.cli_acronyms:main",
            "texbox_tables=texbox.cli_tables:main",
        ]
    },
    python_requires=">=3.6, <=3.8",
    project_urls={
        "Bug Reports": "https://github.com/joaopalmeiro/texbox/issues",
        "Source": "https://github.com/joaopalmeiro/texbox",
    },
)

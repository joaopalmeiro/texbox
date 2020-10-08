import pandas as pd


def parse_args():
    pass


def main():
    data = pd.read_csv(
        "/Users/joao.palmeiro/Documents/GitHub/masters-thesis-meval/data/literature_review_summary.csv"
    )

    print(data)


if __name__ == "__main__":
    main()

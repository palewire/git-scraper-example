# git-scraper-example

A example of a git scraper that downloads, commits and archives a data set.

The source for this demonstration is the list of [liquor stores in the state of Iowa](https://data.iowa.gov/Regulation/Iowa-Liquor-Stores/ykb6-ywnd). The scraping routine is automated by the [scrape.yaml workflow](https://github.com/palewire/git-scraper-example/actions/workflows/scrape.yaml).

## Instructions

Clone the repository

```zsh
git clone git@github.com:palewire/git-scraper-example.git
```

Move into the directory

```zsh
cd git-scraper-example
```

Install the Python tools

```zsh
pipenv install
```

Run the downloader

```zsh
pipenv run python src/download.py
```
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
make download
```

Add your [Big Local News token](https://github.com/biglocalnews/sdk/blob/master/py/tutorial.ipynb) to the environment

```
export BLN_TOKEN=YOURTOKENHERE
```

Run the archive

```zsh
make archive
```

## Contributing

Install dependencies for development

```zsh
pipenv install --dev
```

Run tests

```zsh
make test
```

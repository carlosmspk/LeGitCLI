# LeGit CLI

LeGit aims to validate your git commits, based on scopes defined by you, such as
branch names or authors.

## Install

Currently, the only way to install LeGit CLI is through Python's `pip`. Make
sure that your Python version is 3.8 or higher and run:

```bash
pip install legitcli
```

And that's it, you can verify if installation was succesful by running

```bash
legit version
```

## Usage

Open a terminal on any git repository and run

```bash
legit setup
```

This will add legit as a commit hook and will call it on every commit you
attempt to do. It will also create a `legitrules.yml` file which will dictate
which rules to apply(documentation on this is a WiP, for now, you can check some
[samples](./resources/rulefiles/samples))

And that's it, you're set, any commits will do will first be validated using the
rules file!

However, if you'd like to debug or do some tests mainly on `legitrules.yml`, you
can run the following, which will have no impact on your commits (requires a
text file to be given, which would be the file with the commit message):

```bash
legit validate --verbose --rules-file legitrules.yml COMMIT_MESSAGE_TEXT_FILE
```

## For Contributors

This project uses `poetry` as its package manager. You don't necessarily need
`poetry` as you can simply install required packages with `pip` and run the
project directly from the [main](./src/legitcli/main.py) entry point. However,
you'll require `poetry` to run tests, and it makes life easier to use this
project.

### Setup

You can either:

- Run the setup script (can replace `python3` with whatever command you use):

```bash
python3 ./scripts/setup.py
```

- Or, which is effectively the same, with less checks (can replace `python3`
  with whatever command you use):

```bash
python3 -m venv .venv
poetry env use .venv/bin/python
poetry install --with dev
```

### Running Code

To check that setup was successfuly, you can simply run:

```bash
poetry run legit
```

This should output the command's help and usage. To test the main validation
flow, you can do something like below:

```bash
poetry run legit validate --verbose --rules-file resources/rulefiles/samples/simple.yml resources/message/short_message.txt
```

Overall `poetry run legit` is equivalent to `legit` on release, so you can use
this command to test anything as it would run on release.

To run tests:

```bash
poetry run pytest
```

Finally, to check that build works (does not include tests):

```bash
poetry build
```

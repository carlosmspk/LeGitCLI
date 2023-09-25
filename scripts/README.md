# Development Scripts

Scripts to be executed directly, with the exception of [scriptutils](./scriptutils) which has utils to be imported by the scripts.

Attempting to import anything from this module externally will result in an `ImportError`

### `setup_or_update.py`

Sets up a Python Virtual environment and packages.

```bash
python setup_or_update.py
```

Creates a Python Virtual Environment if none is found and installs python packages from [requirements.txt](../requirements.txt). If Python Virtual environment is already setup, just installs/updates packages

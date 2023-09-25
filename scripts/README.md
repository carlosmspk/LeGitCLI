# Development Scripts

Scripts to be executed directly, with the exception of [scriptutils](./scriptutils) which has utils to be imported by the scripts.

Attempting to import anything from this module externally will result in an `ImportError`

### `create-dummy-git-project.sh`

Create a Subfolder with a Dummy Project for Testing

Script usage: 

```bash
python create-dummy-git-project.py --target "project_name"
```

Creates a folder under `sample_projects` folder, with given name (default is `default` which means project will end up in `sample_projects/default`), adds a single text file and initializes a repo with that file comitted, and with LeGit set up as hook, using [main.py](../main.py) as entry point.
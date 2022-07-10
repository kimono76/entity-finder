# ENTITY FINDER USING MACHINE LEARNING 

## Getting started 
1. Install NeoVim
    [github docs for installing NeoVim](https://github.com/neovim/neovim/wiki/Installing-Neovim)

2. Install Anaconda 
   
    [anaconda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually) 

    [docker image of anaconda](https://hub.docker.com/u/continuumio)

3. Create a virtual environment 
```bash
conda env create -f virtual-environment.yml --prefix ./env
``` 

1. Activate the virtual environment 

```bash
cd ~/source/repos/entity-finder 
conda activate ./env 
``` 
### For updating the current virtual environment
Any package added in the _YAML_ file will be installed
```bash
conda env update --file virtual-environment.yml
```
### For deactivating the current virtual environment
```bash
conda deactivate
```



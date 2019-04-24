**This repository is modified from https://github.com/Satalia/production-data-science.**

# Template

Install **cookiecutter** if you do not have it.

```bash
pip install cookiecutter
```

Clone this repository to the system temporary folder `$TMPDIR`.

```bash
git clone https://github.com/MingChen0919/pyproject_template.git $TMPDIR/pyproject_template
```


Go to the folder where you would like to store the project and create the project template.

```bash
cd <folder_to_store_project>
cookiecutter $TMPDIR/pyproject_template
```

Create a virtual environment and install the package.

```bash
cd <project_name>

# create a new python environment for this project
conda create -n <env_name> python=3.7
# activate the python environment
conda activate <env_name>
# install pandoc, this package is required to run the setup.py
pip install pandoc

pip install -e .
pip freeze | grep -v <package_name> > requirements.txt
git init
git add .
git commit -m "First commit"
git remote add origin <remote_repository_url>.git
git push -u origin master
```


> To remove a conda environment:
> ```bash
> conda env remove --name <env_name>
> ```


Moreover, if you are planning to use the Jupyter Notebook, you have to install the kernel of the environment.

``
python -m ipykernel install --user --name <project_name>
``

Now, create a branch, switch to it,

```bash
git checkout -b <branch_name>
```

and you are ready! 

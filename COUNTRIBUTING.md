# Contribute
First of all I'm very thankfull to you guys all for concidering to contribute to this project.


## Developing
If you already cloned the repository and you know that you need to deep dive in the code, here are some guidelines to set up your environment.
<br>

### Virtual environment with `venv¶`:
You can create a virtual environment in a directory using Python's venv module:
```
$ python -m venv venv
```
That will create a directory ./venv/ with the Python binaries and then you will be able to install packages for that isolated environment.
<br>

### Activate the environment
Activate the new environment with:
```
$ source ./venv/bin/activate (on Linux)
$ .\venv\Scripts\Activate.ps1 (on Windows PowerShell)
```
To check if it worked, use:
```
$ which pip
some/directory/doc-viewer-cli/venv/bin/pip
```
if it shows the `pip` binary at `venv/bin/pip` then it worked. \
Make sure you have the latest pip version on your virtual environment to avoid errorss on the next steps:
```
$ python -m pip install --upgrade pip
```
<br>

### Install packages
Use below pip command so you retreive required packages:
```
$ pip install -r /path-to-project/requirements/development.txt
```

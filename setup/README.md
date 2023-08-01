# Setup for local dev

These are some setup instructions for both Google Cloud AppEngine and a working Python environment via virtual env (+ iPython)

## Google Cloud Setup
For setting up google cloud, start from within your home directory (i.e. `~/`)

This also assumes you have an Google Cloud AppEngine project created. You may also need to setup a service account from within the project (that you can then log into via `gcloud auth login` later)

### Install `gcloud` CLI (linux)
```
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-440.0.0-linux-x86_64.tar.gz
tar -xf google-cloud-cli-440.0.0-linux-x86_64.tar.gz
./google-cloud-sdk/install.sh
```
After this is done, open up a new terminal for changes to take effect
### Initialize `gcloud`
```
./google-cloud-sdk/bin/gcloud init
```
### Authenticate
```
gcloud auth login
```


## Python Setup
For setting up python, this assumes you are within the root directory of this repository.
### Install Python + `pip` (linux)
```
sudo apt-get update
sudo apt-get install python3.8
sudo apt-get install python3-pip
```

### Create/activate python `venv`
```
python -m venv ~/py_envs/dev
source ~/py_envs/dev/bin/activate
```
Note: from this point onward, commands prefixed with `(dev)` indicate you are within the `dev` python virtual environment

### Install `pip` requirements
```
(dev) pip install -r requirements-dev.txt
```

### Setup `ipython` and a profile
```
(dev) mkdir .ipython
(dev) ipython profile create <name> --ipython-dir .ipython
(dev) touch .ipython/profile_<name>/startup/startup.py
(dev) cat setup/ipython/startup.py >> .ipython/profile_<name>/startup/startup.py
```
Note: replace `<name>` with your preferred profile name

### Adding `jobinepy`
Add a `bash` alias to quickly run `ipython` with your pofile `<name>`
```
printf '\nJOBINE_PROFILE="<name>"\n' | cat >> ~/.bashrc
cat setup/ipython/alias.sh >> ~/.bashrc
```

### Running `jobinepy`
```
(dev) jobinepy
Python 3.8.10 (default, May 26 2023, 14:05:08)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.0 -- An enhanced Interactive Python. Type '?' for help.

IPython profile: jobine

In [1]:
```

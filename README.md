# webopenflow
A Bootstrap and Flask-based web GUI for demoing the creation and removal of OpenFlow flows using REST APIs of various controllers.  Currently only OpenDayLight support.


## Installation (Ubuntu)
```
sudo apt-get update
sudo apt-get install python-pip python-dev
pip install Flask
pip install Flask-WTF
pip install virtualenv
```

## Starting
- First, set the correct credentials and controller settings in config.py
```
source webopenflowenv/bin/activate
python run.py
```

- Access the web frontend at http://serverip:8000

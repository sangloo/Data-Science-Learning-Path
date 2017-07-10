## 1. Introduction to Command Line Python ##

/home/dq$ python script.py

## 2. Using Different Python Versions ##

/home/dq$ python3 script.py

## 3. Installing Packages that Extend Python ##

/home/dq$ pip install requests

## 4. Overview of Virtual Environments ##

/home/dq$ virtualenv python2

## 5. Creating a Python 3 virtualenv ##

/home/dq/python3$ virtualenv -p /usr/bin/python3 python3

## 6. Activating a virtualenv ##

/home/dq/python3$ source python3/bin/activate

## 7. Verifying the Installed Packages ##

(python3) /home/dq/python3$ pip freeze

## 8. Importing Saved Functions into a File ##

(python3) /home/dq/python3$ python script.py

## 9. Accessing Command Line Arguments ##

(python3) /home/dq/python3$ python script.py "Hello from the command line"

## 10. Deactivating a virtualenv ##

(python3) /home/dq/python3$ deactivate
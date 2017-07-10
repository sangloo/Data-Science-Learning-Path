## 1. Introduction ##

/home/dq$ ls -l

## 2. Moving Problematic Files to a Separate Folder ##

/home/dq$ mv legislators problematic

## 3. Fixing File Extensions ##

/home/dq/problematic$ cp legislators legislators.csv

## 4. Consolidating Files ##

/home/dq$ mv titanic_survival.csv csv_datasets

## 5. Restricting Permissions ##

/home/dq$ chmod 0740 csv_datasets
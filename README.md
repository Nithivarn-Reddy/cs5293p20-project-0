# cs5293p20-project-0

The main aim of the project is to provide a summary of the nature and count of each nature of the incident that has happended on a particular day in norman.
The data is collected from norman police department website http://normanpd.normanok.gov/content/daily-activity. I am taking an incident report of a particular date and displaying the results based on that report.

### Author - Nithivarn Reddy Shanigaram 

### Email - nithivarn.reddy.shanigaram-1@ou.edu

### Structure

```
└── cs5293p20-project-0
    ├── LICENSE
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── project0
    │   ├── __init__.py
    │   ├── main.py
    │   └── project0.py
    ├── setup.cfg
    ├── setup.py
    └── tests
        ├── test_eincidents.py
        └── test_incidents.py
```

External Packages used 

> PyPDF2

> Pandas

> Pytest

## Steps to install the project

Open your Terminal..

1) git clone the project 

2) Install pipenv in your system 

  - if it is debain based
    Run the following command
    
    pip install pipenv
    
3) cd into cs5293p20-project-0

4) Run pipenv install
  
 This command installs all the dependencies required by the project. (provided in the Pipfile)

## Steps to Run the project

Now run the project using the following command (Inside the cs5293p20-project-0)

 > pipenv run python project0/main.py --incidents Enter-Url
  
  eg : Enter-Url = http://normanpd.normanok.gov/filebrowser_download/657/2020-02-19%20Daily%20Incident%20Summary.pdf
  
This will display the result in your console / terminal.

## To run testcases 
Go inside the virtual environment by running the following commands.

1) cd cs5293p20-project-0

2) Run pipenv shell

3) Run pytest



## Assumptions made in the project are

1) The url provided needs to be a working one.

2) The data present in the multi-line is separated by extra "\n" when it is extracted.

3) Data is Missing in Nature Column only.

4) Missing data is replaced with NULL value.

5) The database is created once with the name "normanpd.db" 

6) The table_name is "incidents" which is dropped everytime.

## External Sources referred

1. pipenv overview [link](https://realpython.com/pipenv-guide/)
2. pandas [link](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
3. Replacing empty spaces in dataframe [link](https://stackoverflow.com/questions/13445241/replacing-blank-values-white-space-with-nan-in-pandas)

### Functionality of each method in project0.py

#### fetchIncidents(url):
     Takes as input the url provided when running the project.
     returns an bytes object.
#### extractIncidents(data):
     Takes as input the bytes object returned from fetchIncidents() method.
     This is the main method where the bytes data is extracted and converted into unicode string . Then the unicode string        is used to extract data from columns and place in it a dataframe.
     Most of the assumptions and edge cases are covered here.
     Data is splitted based on the date.
     returns an dataframe.
#### createDB():
     This method creates a database named "normanpd.db" in the current location where the project is cloned.
     It also creates the table named "incidents".
#### populateDB(incidents,db="normanpd.db"):
     This method takes dataframe generated from extractIncidents as input along with the database name.
     The database name is hardcoded in here, name can be changed as our wish.
     The dataframe is populated into the incidents table. If the table already exits then the table data is dropped.
     returns nothing.
#### status(db="normanpd.db"):
     This method takes as input the db name which is also right now hardcoded, but if needed we can pass a different name.
     This method prints out the nature and the number of occurences of each nature of the incident that has happened on a        particular day.
    

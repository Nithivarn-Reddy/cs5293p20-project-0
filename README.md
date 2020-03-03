# cs5293p20-project-0

The main aim of the project is to provide a summary of the nature and count of each nature of the incident that has happended on a particular day in norman.
The data is collected from norman police department website http://normanpd.normanok.gov/content/daily-activity. I am taking an incident report of a particular date and displaying the results based on that report.

### Author - Nithivarn Reddy Shanigaram 

### Email - nithivarn.reddy.shanigaram-1@ou.edu

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

Now run the project using the following command

  pipenv run python project0/main.py --incidents <url>
  
  eg : <url> = http://normanpd.normanok.gov/filebrowser_download/657/2020-02-19%20Daily%20Incident%20Summary.pdf
  
This will display the result in your console / terminal.

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

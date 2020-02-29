# cs5293p20-project-0

The main aim of the project is to provide a summary of the nature and count of each nature of the incident that has happended on a particular in norman.
The data is collected from norman police department website . I am taking an incident report of a particular date and displaying the results based on that report.

Steps to install the project.

Open your Terminal..

1) git clone the project 

2) Install pipenv in your system 

  - if it is debain based
    Run the following command
    
    pip install pipenv
    
3) cd into cs5293p20-project-0

4) Run    pipenv install
   This command installs all the dependencies required by the project.
   
5) Now run the project using the following command

  pipenv run python project0/main.py --incidents <url>
  
  eg : <url> = http://normanpd.normanok.gov/filebrowser_download/657/2020-02-19%20Daily%20Incident%20Summary.pdf
  
This will display the result in your console / terminal.

Assumptions in the project are:

1) The url you have provided needs to be a working one.

2) The data present in the multi-line is separated by extra "\n" when you extract the data and convert it into a unicode string.

3) Data is missed only in the nature column.

4) Missing data is replaced with NULL value.

5) The database is created once with the name "normanpd.db" 

6) The table_name is "incidents" which is dropped everytime.

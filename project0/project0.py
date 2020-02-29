import urllib.request
import PyPDF2
import tempfile
import re
import pandas as pd
import sqlite3
from sqlite3 import Error


#df= pd.DataFrame(columns=['incident_time','incident_number','incident_location','nature','incident_ori'])
#getting the pdf file from the page which is provided as URL
def fetchIncidents(url):
    #url = ("http://normanpd.normanok.gov/filebrowser_download/657/2020-02-05%20Daily%20Incident%20Summary.pdf")
    data=urllib.request.urlopen(url).read()
    return data


def extractIncidents(data):
    """
        Here we extract the data pulled from the website and parse it using a pdfReader.
        args:
            data : which is returned by the fetchIncidents(url)
        returns:
            pdfReader object.
    """
    df = pd.DataFrame(columns=['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori'])
    fh =tempfile.TemporaryFile()
    fh.write(data)
    fh.seek(0)
    pdfReader = PyPDF2.pdf.PdfFileReader(fh)
    for page in range(pdfReader.getNumPages()):
        pageData = pdfReader.getPage(page).extractText()
        # cleaning process starts
        if page == 0:
            if (pageData.find("NORMAN POLICE DEPARTMENT")):
                x = pageData.find("NORMAN POLICE DEPARTMENT")
                pageData = pageData[:x]
        if page == pdfReader.getNumPages() - 1:
            if pageData.endswith("\n"):
                pageData = pageData[:-1]
            pageData = pageData[:pageData.rfind("\n")]
        if pageData.endswith("\n"):
            pageData = pageData[:-1]
        # matching the data to get date and replacing the \n infornt of it with ';;'
        m = re.search(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", pageData).group()
        pageData = pageData.replace('\n' + m, ';;' + m)

        # splitting it into list of records

        records = pageData.split(";;")

        # Handling multiline address
        for index, record in enumerate(records):
            count = record.count("\n")
            if count == 4:
                continue
            elif count > 4:
                record = record.replace("\n", ";;", 2)
                count = record.count("\n")
                record = record.replace("\n", "", count - 2).replace(";;", "\n")
                records[index] = record
            elif count < 4:
                idx = record.rfind("\n")
                record = record[:idx] + "\n" + record[idx:]
                records[index] = record
        dataFrame = pd.DataFrame([record.split('\n') for record in records],
                                 columns=['incident_time', 'incident_number', 'incident_location', 'nature',
                                          'incident_ori'])
        df = df.append(dataFrame, ignore_index=True)
    df = df.drop(df.index[0])
    df[df == ''] = "NULL"
    return df
    #return pdfReader


#url = ("http://normanpd.normanok.gov/filebrowser_download/657/2020-02-24%20Daily%20Incident%20Summary.pdf")
#pdfReader = extractIncidents(fetchIncidents(url))
def createDB():
    try:
        connection = sqlite3.connect(r"normanpd.db")
        con = connection.cursor()
        con.execute('''Create table incidents(
        incident_time TEXT,
        incident_number TEXT,
        incident_location TEXT,
        nature TEXT,
        incident_ori TEXT
        );''')
        connection.commit()
        connection.close()
    except Error as e:
        print(e)

def populatedb(incidents,db="normanpd.db"):
    """
        This method populates the db with the data generated
        args:
            db: db name to connect to
            incidents :a dataframe whose data is inserted into sql.[pandas object]
    """
    try:
        dbconn = sqlite3.connect("./"+db)
    except Error:
        print("unable to establish connection")
    cur = dbconn.cursor()
    incidents.to_sql("incidents",dbconn,if_exists="replace",index=False)
    dbconn.commit()
    dbconn.close()


def status(db="normanpd.db"):
    dbconn=sqlite3.connect("./"+db)
    cur =dbconn.cursor()
    for row in cur.execute("select nature,count(*) from incidents group by nature order by nature"):
        print(row[0]+"|",row[1])
    dbconn.close()

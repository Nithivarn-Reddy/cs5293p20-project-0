from project0 import *
from subprocess import check_output



url = "http://normanpd.normanok.gov/filebrowser_download/657/2020-02-24%20Daily%20Incident%20Summary.pdf"


def test_eincidents():
    assert extractIncidents(fetchIncidents(url)).shape[1] == 5 # to check number of columns = 5
def test_createDB():
    createDB()
    assert "normanpd.db" in str(check_output(["ls","-l"]))

def test_populateDB():
    populatedb(extractIncidents(fetchIncidents(url)))
    dbconn = sqlite3.connect(r"/home/nithivarn/TextAnalytics/cs5293p20-project-0/normanpd.db")
    cur = dbconn.cursor()
    cur.execute("Select * from incidents")
    assert len(cur.fetchall()) > 0
    dbconn.close()

def test_status():
    dbconn = sqlite3.connect(r"/home/nithivarn/TextAnalytics/cs5293p20-project-0/normanpd.db")
    cur = dbconn.cursor()
    cur.execute("select nature,count(*) from incidents group by nature order by nature")
    assert len(cur.fetchall()) > 0
    dbconn.close()

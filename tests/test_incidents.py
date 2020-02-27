from project0 import fetchIncidents




url = "http://normanpd.normanok.gov/filebrowser_download/657/2020-02-24%20Daily%20Incident%20Summary.pdf"
def test_fetchIncidents():
    assert fetchIncidents(url) is not None




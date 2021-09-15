import requests

def load_xml_data(url):
    url = 'https://www.w3schools.com/xml/plant_catalog.xml'

    resp = requests.get(url)

    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)
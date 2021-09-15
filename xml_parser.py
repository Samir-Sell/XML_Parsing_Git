import xml.etree.ElementTree as ET



def parse_xml(xmlfile):
    
    tree = ET.parse(xmlfile) # Parse the tree structure of the XML file. This creates an element tree object

    root = tree.getroot() # Access the root element 
    item_list = []
    
    for item in root.findall('./PLANT'): # Use xpath syntax to pull out xml tags
        plant = {}
        for data in item.getchildren():
            plant[data.tag] = data.text
        item_list.append(plant)


    return item_list
        




parse_xml(r"C:\Users\ssellars\Documents\CJOC\XML_Parsing\topnewsfeed.xml")
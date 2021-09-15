from load_data import load_xml_data
from xml_parser import parse_xml
from convert_to_df_csv import convert_list_dict

def main():
    
    load_xml_data('https://www.w3schools.com/xml/plant_catalog.xml')
    
    item_list = parse_xml(r"C:\Users\ssellars\Documents\CJOC\XML_Parsing\topnewsfeed.xml")
    print(item_list)
    convert_list_dict(item_list)


if __name__ == "__main__":
    main()
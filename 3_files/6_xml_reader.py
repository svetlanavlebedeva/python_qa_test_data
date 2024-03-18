import xml.etree.ElementTree as ET

from files import XML_FILE_PATH

# Load and parse the XML file
tree = ET.parse(XML_FILE_PATH)
root = tree.getroot()

# Iterate through each book in the library
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    print(f'Title: {title}, Author: {author}, Year: {year}')

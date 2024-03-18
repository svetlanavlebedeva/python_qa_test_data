import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('example.xml')
root = tree.getroot()

# Iterate through each book in the library
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    print(f'Title: {title}, Author: {author}, Year: {year}')

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString


def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = tostring(elem, 'utf-8')
    reparsed = parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


# Create the base element
library = Element('library')

# Add books to the library
book = SubElement(library, 'book')
title = SubElement(book, 'title')
title.text = 'Python Crash Course'
author = SubElement(book, 'author')
author.text = 'Eric Matthes'
year = SubElement(book, 'year')
year.text = '2016'

# Convert to a pretty-printed XML string
pretty_xml = prettify(library)

# Write to file
with open('new_library.xml', 'w') as xml_file:
    xml_file.write(pretty_xml)

print(pretty_xml)

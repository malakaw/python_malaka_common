#https://docs.python.org/2/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
tree = ET.parse('d1.xml')
root = tree.getroot()
for move in root.iter('furl'):
    print move.text

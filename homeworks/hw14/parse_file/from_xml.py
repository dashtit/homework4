import xml.etree.ElementTree as ET


def read_xml(filename):
    tree = ET.parse(filename)
    return tree


def calculate_total_cost(filename):
    tree = read_xml(filename)
    total_cost = 0
    for item in tree.findall('item'):
        total_cost += float(item.find('price').text) * float(item.find('quantity').text)
    return total_cost

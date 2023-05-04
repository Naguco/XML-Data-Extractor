# import xml.etree.ElementTree as ET

# tree = ET.parse('./data.xml')
# root = tree.getroot()

# print([x.text for x in root.findall(".//event_reason")])

import xmltodict
import sys

# Read the XML file
with open("data.xml", "r") as xml_file:
    xml = xml_file.read()

# Parse the XML into a dictionary
json = xmltodict.parse(xml)

# Get the path to the roots of the XML document from the input of the user
root_path = sys.argv[1]

# Split the path into an array of the different nodes
root_path_array = root_path.split("/")

# Get the nodes from the user inputs after the root node
nodes = sys.argv[2:]

def next_step(step, obj):
    if root_path_array[step] == root_path_array[-1]:
        if isinstance(obj[root_path_array[step]], list):
            for item in obj[root_path_array[step]]:
                write_node(item)
        else:
            write_node(obj[root_path_array[step]])
        return
    if root_path_array[step] not in obj:
        print(root_path_array[step])
        raise ValueError('The path is not correct!')
    if isinstance(obj[root_path_array[step]], list):
        for i, item in enumerate(obj[root_path_array[step]]):
            print(f"-----------{root_path_array[step]}{i+1}-----------")
            next_step(step + 1, item)
            print("--------------------------------")
    else:
        next_step(step + 1, obj[root_path_array[step]])

def write_node(obj):
    info = []
    for node in nodes:
        if node not in obj:
            info.append("N/A")
        else:
            info.append(str(obj[node]))
    print(",".join(info))

next_step(0, json)
from lxml import etree
import xml.etree.ElementTree as ET

tree = ET.parse("fichero.xml")
root = tree.getroot()
eventos = []
dia = []
for neighbor in root.iter('atributo'):
    if neighbor.attrib['nombre'] == "TITULO":
        eventos.append(neighbor.text)
    if neighbor.attrib['nombre'] == "FECHA-EVENTO":
        dia.append(neighbor.text)
final_list = []


def generate_xml(eventos, dia):
    root = ET.Element('tipo')
    for i in range(len(eventos)):
        m1 = ET.SubElement(root, 'evento')
        m2 = ET.SubElement(m1, 'fecha')
        m2.text = dia[i]
        m3 = ET.SubElement(m1, 'titulo')
        m3.text = eventos[i]
    tree = ET.ElementTree(root)
    tree.write('Output.xml')


generate_xml(eventos, dia)

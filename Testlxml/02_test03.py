from lxml import etree
import os
path = os.path.abspath(os.path.dirname(__file__))

root = etree.Element("root")
root.text = "TEXT"
print(root.text)
print('*'*20)
print(etree.tostring(root))
print('*'*20)
html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = "TEXT"

print(etree.tostring(html))

br = etree.SubElement(body, "br")
print(etree.tostring(html))

br.tail = "TAIL"
print(etree.tostring(html))
print('*'*20)
print(etree.tostring(br))
print(etree.tostring(br, with_tail=False)) # lxml.etree only!
print('*'*20)
print(etree.tostring(html, method="text"))
print('*'*20)

#Extraction
print(html.xpath("string()")) # lxml.etree only!
print(html.xpath("//text()")) # lxml.etree only!
print(etree.XPath("//text()")(html)) # lxml.etree only!
print('*'*20)
build_text_list = etree.XPath("//text()") # lxml.etree only!
print(build_text_list(html))
print('*'*20)
print(etree.tostring(html, pretty_print=True).decode())
print('*'*20)
#Hiérérachie
texts = build_text_list(html)
print(texts[0])
parent = texts[0].getparent()
print(parent.tag)
print(texts[1])
print(texts[1].getparent().tag)
print('*'*20)
#itérer dans l'arborescence
root = etree.Element("root")
etree.SubElement(root, "child").text = "Child 1"
etree.SubElement(root, "child").text = "Child 2"
etree.SubElement(root, "another").text = "Child 3"

#prettyprint(root)
print(etree.tostring(root, pretty_print=True).decode())


for element in root.iter():
    print(f"{element.tag} - {element.text}")
    
print('*'*20)
for element in root.iter("child"):
    print(f"{element.tag} - {element.text}")
print('*'*20)
for element in root.iter("another", "child"):
    print(f"{element.tag} - {element.text}")
print('*'*20)
for element in root.iterchildren():
    print(f"{element.tag} - {element.text}")
print('*'*20)
for element in root.iterchildren("child"):
    print(f"{element.tag} - {element.text}")
print('*'*20)
root.append(etree.Entity("#234"))
root.append(etree.Comment("some comment"))
print(etree.tostring(root, pretty_print=True).decode())

for element in root.iter():
    if isinstance(element.tag, str):
        print(f"{element.tag} - {element.text}")
    else:
        print(f"SPECIAL: {element} - {element.text}")
print('*'*20)
for element in root.iter(tag=etree.Element):
    print(f"{element.tag} - {element.text}")
print('*'*20)
for element in root.iter(tag=etree.Comment):
    print(f"{element.tag} - {element.text}")
print('*'*20)
for element in root.iter(tag=etree.Entity):
    print(f"{element.tag} - {element.text}")
print('*'*20)
#Sérialisation
root = etree.XML('<root><a><b/></a></root>')
print(etree.tostring(root, pretty_print=True).decode())
print('*'*20)
xml_string = etree.tostring(root, xml_declaration=True)
print(xml_string.decode(), end='')
print()
print('*'*20)
latin1_bytesstring = etree.tostring(root, encoding='iso8859-1')
print(latin1_bytesstring.decode('iso8859-1'), end='')
print()
print('*'*20)
print(etree.tostring(root, pretty_print=True).decode(), end='')
#prettyfy
print()
print('*'*20)
root = etree.XML('<root><a><b/>\n</a></root>')
print(etree.tostring(root).decode())
print('*'*20)
etree.indent(root)
print(etree.tostring(root).decode())
print('*'*20)
print(etree.tostring(root))
print('*'*20)
etree.indent(root, space="    ")
print(etree.tostring(root).decode())
print('*'*20)
etree.indent(root, space="\t")
print(etree.tostring(root))
print('*'*20)
#Gestion HTML
root = etree.XML(
    '<html><head/><body><p>Hello<br/>World</p></body></html>')
print(etree.tostring(root))
print('*'*20)
print(etree.tostring(root, method='xml'))
print('*'*20)
print(etree.tostring(root, method='html'))
print('*'*20)
print(etree.tostring(root, method='html', pretty_print=True).decode())
print('*'*20)
#Class ElementTree
root = etree.XML( 
'''\
    <!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
    <root>
        <a>&tasty;</a>
    </root>
''')
tree = etree.ElementTree(root)
print(tree.docinfo.xml_version)
print(tree.docinfo.doctype)
tree.docinfo.public_id = '-//W3C//DTD XHTML 1.0 Transitional//EN'
tree.docinfo.system_url = 'file://local.dtd'
print(tree.docinfo.doctype)
print('*'*20)
etree.indent(root, space="\t")
print(etree.tostring(tree, pretty_print=True).decode())

print('*'*20)
#Analyse à partir de chaînes et de fichiers
some_xml_data = "<root>data</root>"

root = etree.fromstring(some_xml_data)
print(root.tag)
print(etree.tostring(root))
#Spécifique XML et HTML
root = etree.XML("<root>data</root>")
print(root.tag)
print(etree.tostring(root))

root = etree.HTML("<p>data</p>")
print(etree.tostring(root))
print('*'*20)
#parse à utiliser pour les fichiers
tree = etree.parse(f"{path}\\data.xml")

print(etree.tostring(tree))
print('*'*20)
root = tree.getroot()
print(root.tag)
print(etree.tostring(root))

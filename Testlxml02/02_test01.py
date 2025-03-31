from lxml import etree

root = etree.Element("root")
print(root.tag)
print('*'*20)
#*********************************************************
root.append( etree.Element("child1") )

child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

etree.tostring(root)

def prettyprint(element, **kwargs):
    xml = etree.tostring(element, pretty_print=True, **kwargs)
    print(xml.decode(), end='')
    
prettyprint(root)
print('*'*20)
#*********************************************************
#Les éléments sont des listes

child = root[0]
print(child.tag)
print(len(root))
print(root.index(root[1]))  # lxml.etree only!
print('*'*20)

children = list(root)

for child in root:
    print(child.tag)

print('*'*20)

root.insert(0, etree.Element("child0"))
start = root[:1]
end   = root[-1:]

print(start[0].tag)
print(end[0].tag)
print('*'*20)
if len(root):                 # test if it has children
    print("The root element has children")
print('*'*20)

child = root[1]
print(child.getprevious().tag) 
print(child.getnext().tag)
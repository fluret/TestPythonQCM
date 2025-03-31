from lxml import etree

root = etree.Element("root")
root = etree.Element("root", interesting="totally")
print(etree.tostring(root))
print('*'*20)
root.set("hello", "Huhu")
print(root.get("hello"))
print(etree.tostring(root))
print('*'*20)
print(sorted(root.keys()))

for name, value in sorted(root.items()):
    print(f'{name} =  {value}')
print('*'*20)
attributes = root.attrib
print(attributes)
print('*'*20)
print(root.attrib["hello"])
print('*'*20)
print(root.attrib["interesting"])
print('*'*20)
print(attributes.get("no-such-attribute"))
attributes["hello"] = "Guten Tag"
print(attributes["hello"])
print(root.get("hello"))
print('*'*20)
d = dict(root.attrib)
print(sorted(d.items()))
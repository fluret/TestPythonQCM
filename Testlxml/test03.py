from lxml import etree

users = etree.Element("users")
user = etree.SubElement(users, "user")
user.set("data-id", "101")
nom = etree.SubElement(user, "nom")
nom.text = "Zorro"
metier = etree.SubElement(user, "metier")
metier.text = "Danseur"
print(etree.tostring(users, pretty_print=True))
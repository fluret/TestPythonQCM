from lxml import etree
import os
path = os.path.abspath(os.path.dirname(__file__))


tree = etree.parse(f"{path}\\data.xml")
for user in tree.xpath("/users/user/nom"):
    print(user.text)
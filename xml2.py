import xml.etree.ElementTree as ET
data = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Kyama</name>
            <age>24</age>
        </user>
        <user x="1">
            <id>002</id>
            <name>Katheu</name>
            <age>21</age>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Age:', item.find('age').text)
    print('Attribute:', item.get("x"))
    print('')
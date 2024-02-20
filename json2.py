import json
data = '''[
{
    "id" : "001",
    "x" : "2",
    "name" : "Rubies"
},
{
    "id" : "002",
    "x" : "7",
    "name" : "Jewel"
}
]'''

users = json.loads(data)
#print(users)
for user in users:
    print('ID:', user['id'])
    print('Attribute:', user['x'])
    print('Name:', user['name'])
    print('')
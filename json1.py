import json
data = '''{
"name" : "Rubies",
"phone" : {
    "type" : "intl",
    "number" : "+25471079113"
},
"email" : {
    "hide" : "yes"
}
}'''

user = json.loads(data)
print('Name:', user['name'])
print('Phone:', user['phone']['number'])
print('Hide:', user['email']['hide'])
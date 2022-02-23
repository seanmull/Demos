from irisclient import IrisClient

client = IrisClient(
    app='Autoalerts',
    key='a7a9d7657ac8837cd7dfed0b93f4b8b864007724d7fa21422c24f4ff0adb2e49',
    api_host='http://localhost:16649'
)
# create an incident
print(client.incident('Example Plan', context={'key_foo': 'abc', 'key_bar': 1}))
# send an adhoc notification
# print client.notification(role='user', target='Phone 1', priority='urgent', subject='Yo')


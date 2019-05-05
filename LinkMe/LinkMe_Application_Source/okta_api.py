import requests
import json

def get_users():
    url = 'https://dev-259906.okta.com/api/v1/groups/00gj4tmrhPMM8knsL356/users'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
               'Authorization': 'SSWS 00KMgmBW8eDf23-nQBvuLaCdkgsW7dj0GoQQSl5bkJ'}
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)

    users = []
    for i, val in enumerate(data):
        users.append(val[0]['profile']['login'])

    return users

def check_if_dev(login_info):
    if login_info in get_users():
        return True
    else:
        return False

from requests_oauthlib import OAuth1Session

import config

aweber = OAuth1Session(client_key=config.CLIENT_KEY,
                       client_secret=config.CLIENT_SECRET,
                       resource_owner_key=config.RESOURCE_OWNER_KEY,
                       resource_owner_secret=config.RESOURCE_OWNER_SECRET)

account_id = input('Enter account id: ')
list_id = input('Enter list id: ')
url = 'https://api.aweber.com/1.0/accounts/{}/lists/{}/subscribers'.format(account_id, list_id)

email = input('Enter a email: ')
data = {'email': email,
        'ws.op': 'create'}

response = aweber.post(url, data=data)

if response.status_code == 201:
    print('Subscriber {} added to list {}'.format(email, list_id))
else:
    print('Error: {}'.format(response.status_code))

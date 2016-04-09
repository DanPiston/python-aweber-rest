from requests_oauthlib import OAuth1Session
from pprint import pprint

import config

aweber = OAuth1Session(client_key=config.CLIENT_KEY,
                       client_secret=config.CLIENT_SECRET,
                       resource_owner_key=config.RESOURCE_OWNER_KEY,
                       resource_owner_secret=config.RESOURCE_OWNER_SECRET)

url = 'https://api.aweber.com/1.0/accounts'


response = aweber.get(url)

pprint (response.json())

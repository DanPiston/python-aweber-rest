from requests_oauthlib import OAuth1Session
from urllib.parse import urlencode
import sys
from aweber_rest import config

def get_resource_auth(client_key, client_secret):
    callback_uri = 'http://localhost/'

    oauth = OAuth1Session(client_key
                         ,client_secret = client_secret
                         ,callback_uri = callback_uri)

    request_token_uri = 'https://auth.aweber.com/1.0/oauth/request_token'
    fetch_response = oauth.fetch_request_token(request_token_uri)

    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')

    base_auth_url = 'https://auth.aweber.com/1.0/oauth/authorize?'
    auth_url = oauth.authorization_url(base_auth_url)

    print('Authorize here:', auth_url)
    redirect_response = input('Enter the redirect URL: ')

    oauth_response = oauth.parse_authorization_response(redirect_response)
    verifier = oauth_response.get('oauth_verifier')

    access_token_url = 'https://auth.aweber.com/1.0/oauth/access_token'

    aweber_access = OAuth1Session(client_key
                         ,client_secret = client_secret
                         ,resource_owner_key = resource_owner_key
                         ,resource_owner_secret = resource_owner_secret
                         ,verifier = verifier)
    aweber_access_tokens = aweber_access.fetch_access_token(access_token_url)

    resource_owner_key = aweber_access_tokens['oauth_token']
    resource_owner_secret = aweber_access_tokens['oauth_token_secret']

    return (resource_owner_key, resource_owner_secret)


def get_resource_tokens():
    (resource_owner_key, resource_owner_secret) = get_resource_auth(config.CLIENT_KEY, config.CLIENT_SECRET)
    print("RESOURCE_OWNER_KEY = '" + resource_owner_key + "'")
    print("RESOURCE_OWNER_SECRET = '" + resource_owner_secret + "'")
    sys.exit()


def call(url, args):
    if args:
        url += '?{0}'.format(urlencode(args))

    aweber_access = OAuth1Session(config.CLIENT_KEY
                        ,client_secret = config.CLIENT_SECRET
                        ,resource_owner_key = config.RESOURCE_OWNER_KEY
                        ,resource_owner_secret = config.RESOURCE_OWNER_SECRET)
    return aweber_access.get(url)
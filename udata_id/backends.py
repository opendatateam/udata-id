import json
import requests
from social.backends.oauth import BaseOAuth2
from urllib import urlencode


class IDOAuth2(BaseOAuth2):
    """ID OAuth authentication backend"""
    name = 'id'
    AUTHORIZATION_URL = 'http://localhost:8000/oauth/authorize/'
    ACCESS_TOKEN_URL = 'http://localhost:8000/oauth/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ' '
    DEFAULT_SCOPE = ['read']
    STATE_PARAMETER = ''
    EXTRA_DATA = []

    def get_user_details(self, response):
        """Return user details from ID account"""
        return response

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'http://localhost:8000/account/user/?' + urlencode({
            'access_token': access_token
        })
        try:
            return requests.get(url).json()
        except ValueError:
            return None

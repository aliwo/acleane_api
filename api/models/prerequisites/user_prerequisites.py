from datetime import datetime

import requests
from flask import request, g

from api.models.prerequisites.helper import PrerequisitesHelper
from api.models.prerequisites.prerequisites import Prerequisites
from api.models.user import User
from libs.database.engine import Session
from libs.route.errors import ClientError
from libs.status import Status

helper = PrerequisitesHelper(User, 'json')

class UserPrerequisites(Prerequisites):

    base_model = User

    OAUTH_PARTIES = {
        'google': 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json',
        'kakao': 'https://kapi.kakao.com/v2/user/me',
        'naver': 'https://openapi.naver.com/v1/nid/me'
    }

    def kakao(self):
        self._on_create('kakao')

    def naver(self):
        self._on_create('naver')

    def google(self):
        self._on_create('google')

    def facebook(self):
        '''
        facebook 만 방식이 살짝 다릅니다.. 이놈의 graphql...
        '''
        resp = requests.get(f'https://graph.facebook.com/me?access_token={request.json.get("token")}&fields=id,name,email,picture')
        if resp.status_code != 200:
            raise ClientError('invalid token', Status.HTTP_400_BAD_REQUEST)
        g.info = resp.json()

    def apple(self):
        if not request.json.get('code'):
            raise ClientError('invalid auth code', Status.HTTP_400_BAD_REQUEST)

    def _on_create(self, party):
        resp = requests.get(self.OAUTH_PARTIES[party],
                            headers={'Authorization': f'Bearer {request.json.get("token")}'})
        if resp.status_code != 200:
            raise ClientError('invalid token', Status.HTTP_400_BAD_REQUEST)
        g.info = resp.json()

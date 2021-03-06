from flask import request
from api.models.user_session import UserSession


def user_session_or_none():
    '''
    세션의 만료, 동결 여부를 묻지 않고 세션을 리턴하는 헬퍼함수입니다.
    :return:
    '''
    token = request.headers.get('Authorization', None)
    if token is not None and (len(token.split()) >= 2):
        token = token.split()[1]
        user_session = UserSession.get_session(token)
        return user_session
    return None


def user_or_none():
    user_session = user_session_or_none()
    if user_session:
        return user_session.user
    return None


def user_id_or_zero():
    user = user_or_none()
    if user:
        return user.id
    return 0

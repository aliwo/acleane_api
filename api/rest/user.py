from flask import g

from libs.route.router import route
from libs.status import Status


@route
def get_my_profile():
    return {'user': g.user_session.user.json()}, Status.HTTP_200_OK



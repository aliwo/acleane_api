from datetime import datetime

from flask import g, request

from api.models.user import User
from libs.database.engine import Session
from libs.route.router import route
from libs.status import Status


@route
def get_my_profile():
    return {'user': g.user_session.user.json()}, Status.HTTP_200_OK


@route
def put_user_profile():
    for key, value in request.json.items():
        setattr(g.user_session.user, key, value)
        Session(changed=True)
    g.user_session.user.el_time = datetime.now()
    Session().commit()
    return {'user': g.user_session.user.json()}, Status.HTTP_200_OK

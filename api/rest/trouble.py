from flask import g, request

from api.models.trouble import Trouble
from api.models.user_trouble import UserTrouble
from libs.database.engine import Session, afr
from libs.status import Status


def get_all_troubles():
    return [x.json() for x in Session().query(Trouble).all()], Status.HTTP_200_OK


def get_all_user_trouble():
    return [x.json() for x in Session().query(UserTrouble).filter((UserTrouble.user_id == g.user_session.user.id)).all()]\
        , Status.HTTP_200_OK


def post_user_troubles():
    afr(UserTrouble(user_id=g.user_session.user.id, trouble_id=request.json.get('trouble_id')))
    Session().commit()
    return {'okay'}, Status.HTTP_200_OK



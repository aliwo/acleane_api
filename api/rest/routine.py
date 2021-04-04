from flask import g, request

from api.models.routine import Routine
from api.models.amount import Amount
from api.models.user_routine import UserRoutine
from libs.database.engine import Session, afr
from libs.status import Status


def get_all_routines():
    return [x.json() for x in Session().query(Routine).all()], Status.HTTP_200_OK


def get_all_user_routines():
    return [x.json() for x in Session().query(UserRoutine).filter(UserRoutine.user_id == g.user_session.user.id).all()]\
        , Status.HTTP_200_OK


def post_user_routines():
    for routine_id, amount in zip(request.json.get('routine_id'), request.json.get('amounts')):
        afr(UserRoutine(user_id=g.user_session.user.id, routine_id=routine_id, amount=amount))
    Session().commit()
    return {'okay'}, Status.HTTP_200_OK


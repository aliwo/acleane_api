from flask import g, request

from api.models.routine import Routine
from api.models.amount import Amount
from api.models.user_routine import UserRoutine
from libs.database.engine import Session, afr
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def get_all_routines():
    return [x.json() for x in Session().query(Routine).all()], Status.HTTP_200_OK


@route
def get_all_user_routines():
    return [x.json() for x in Session().query(UserRoutine).filter(UserRoutine.user_id == g.user_session.user.id).all()]\
        , Status.HTTP_200_OK


@route
def post_user_routines():
    for routine_id in request.json.get('routine_ids', []):
        if Session().query(UserRoutine).filter_by(user_id=g.user_session.user.id, routine_id=routine_id).first():
            raise ClientError(f'duplicate routine id: #{routine_id}')

    for routine_id, amount in zip(request.json.get('routine_ids', []), request.json.get('amounts', [])):
        user_routine = afr(UserRoutine(user_id=g.user_session.user.id, routine_id=routine_id, amount=amount))
        user_routine.name = user_routine.routine.name
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


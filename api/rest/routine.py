from flask import g, request
from sqlalchemy.orm.exc import NoResultFound

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
    for routine_id, amount in zip(request.json.get('routine_ids', []), request.json.get('amounts', [])):
        user_routine = Session().query(UserRoutine).filter_by(user_id=g.user_session.user.id, routine_id=routine_id).first()
        if not user_routine:
            user_routine = afr(UserRoutine(user_id=g.user_session.user.id, routine_id=routine_id))
        user_routine.amount = amount
        user_routine.name = user_routine.routine.name
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def put_user_routine(user_routine_id):
    try:
        user_routine = Session().query(UserRoutine).filter_by(id=user_routine_id, user_id=g.user_session.user.id).one()
    except NoResultFound:
        raise ClientError(f'no user routine found #{user_routine_id}')

    if request.json.get('routine_id'):
        routine = Session().query(Routine).filter_by(id=request.json.get('routine_id')).one()
        user_routine.routine_id = routine.id
        user_routine.name = routine.name

    if request.json.get('amount'):
        user_routine.amount = request.json.get('amount')

    Session().commit()
    return user_routine.json(), Status.HTTP_200_OK


@route
def delete_user_routine(user_routine_id):
    try:
        user_routine = Session().query(UserRoutine).filter_by(id=user_routine_id, user_id=g.user_session.user.id).one()
    except NoResultFound:
        raise ClientError(f'no user routine found #{user_routine_id}')
    Session().delete(user_routine)
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


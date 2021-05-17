from datetime import datetime

from flask import g, request
from sqlalchemy import extract
from sqlalchemy.orm.exc import NoResultFound

from api.models.journal import Journal
from api.models.user import User
from libs.database.engine import afr, Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status


@route
def get_all_journals_of_month():
    journals = Session().query(Journal).filter(
        (Journal.user_id == g.user_session.user.id)
        & (extract('year', Journal.date) == int(request.args.get('year')))\
        & (extract('month', Journal.date) == int(request.args.get('month')))
    )
    return [x.json() for x in journals], Status.HTTP_200_OK


@route
def create_journal():
    '''
    유저 하나에 락을 걸어야 되는거 같은데
    락을 걸고 특정 날짜 + 특정 유저 + 특정 routine_id 가 중복되는 row 가 있는지 찾고, 만약 있다면 추가하면 안 됨
    '''
    date = datetime.strptime(request.json.get('date'), '%Y-%m-%d').date()
    user = Session().query(User).filter_by(id=g.user_session.user.id).with_for_update().one()
    duplicate = Session().query(Journal).filter(
        (Journal.user_id == g.user_session.user.id)
        & (Journal.routine_id == request.json.get('routine_id'))
        & (Journal.date == date)
    ).first()

    if duplicate:
        raise ClientError('duplicate journal')

    afr(
        Journal(user_id=g.user_session.user.id,
                routine_id=request.json.get('routine_id'),
                date=date
        )
    )
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK


@route
def delete_journal(journal_id):
    try:
        journal = Session().query(Journal).filter_by(id=journal_id, user_id=g.user_session.user.id).one()
    except NoResultFound:
        raise ClientError(f'no journal found #{journal_id}')

    Session().delete(journal)
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK

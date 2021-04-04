from datetime import datetime

from flask import g, request
from sqlalchemy import extract

from api.models.journal import Journal
from libs.database.engine import afr, Session
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
    afr(
        Journal(user_id=g.user_session.user.id,
                routine_id=request.json.get('routine_id'),
                date=datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
        )
    )
    Session().commit()
    return {'okay'}, Status.HTTP_200_OK






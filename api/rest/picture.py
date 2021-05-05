from datetime import datetime

from api.models.picture import Picture
from libs.database.engine import afr, Session
from libs.route.errors import ClientError
from libs.route.router import route
from libs.status import Status
from libs.storage import gcs, s3
from flask import request, g


@route
def upload_picture():
    file = request.files.get('image')
    url = s3.upload_file(file, file.filename)
    picture = afr(
        Picture(
            user_id=g.user_session.user.id,
            url=url,
            date=datetime.strptime(request.form.get('date'), '%Y-%m-%d').date(),
        )
    )
    Session().commit()
    return picture.json(), Status.HTTP_200_OK


@route
def get_picture_by_id(picture_id):
    try:
        picture = Session().query(Picture).filter_by(id=picture_id).one()
    except:
        raise ClientError(f'picture id #{picture_id} not found', Status.HTTP_404_NOT_FOUND)
    if picture.user_id != g.user_session.user.id:
        raise ClientError('not your picture')

    return picture.json(), Status.HTTP_200_OK


@route
def get_picture_by_date(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    picture = Session().query(Picture).filter_by(date=date).first()
    if not picture:
        return {}, Status.HTTP_200_OK
    if picture.user_id != g.user_session.user.id:
        raise ClientError('not your picture')
    return picture.json() if picture else {}, Status.HTTP_200_OK


@route
def delete_picture_by_id(picture_id):
    try:
        picture = Session().query(Picture).filter_by(id=picture_id).one()
    except:
        raise ClientError(f'picture id #{picture_id} not found', Status.HTTP_404_NOT_FOUND)
    if picture.user_id != g.user_session.user.id:
        raise ClientError('not your picture')
    Session().delete(picture)
    Session().commit()
    return {'okay': True}, Status.HTTP_200_OK

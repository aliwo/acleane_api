from datetime import datetime

from api.models.picture import Picture
from libs.database.engine import afr, Session
from libs.route.router import route
from libs.status import Status
from libs.storage import gcs, s3
from flask import request, g


@route
def upload_picture():
    file = request.files.get('image')
    url = s3.upload_file(file, file.filename)
    afr(Picture(user_id=g.user_session.user.id, url=url))
    Session().commit()
    return {'url': url}, Status.HTTP_200_OK
from api.models.picture import Picture
from libs.database.engine import afr, Session
from libs.route.router import route
from libs.status import Status
from libs.storage import gcs
from flask import request, g


@route
def upload_picture():
    '''
    TODO: picture 에 날짜 값도 넣도록 수정해야 함
    '''
    file = request.files.get('image')
    url = gcs.upload_file(file.read(), file.filename, file.content_type)
    afr(Picture(user_id=g.user_session.user.id, url=url))
    Session().commit()
    return {'url': url}, Status.HTTP_200_OK

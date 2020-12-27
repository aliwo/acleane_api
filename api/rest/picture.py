from datetime import datetime

from api.models.picture import Picture
from libs.database.engine import afr, Session
from libs.route.router import route
from libs.status import Status
from libs.storage import gcs
from flask import request, g


@route
def upload_picture():
    '''
    TODO: 사진은 form 데이터니까, 추가 정보는 form 에서 받아야 할 거임. 테스트 해보기
    '''
    file = request.files.get('image')
    url = gcs.upload_file(file.read(), file.filename, file.content_type)
    afr(
        Picture(user_id=g.user_session.user.id,
                url=url,
                date=datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
        )
    )
    Session().commit()
    return {'url': url}, Status.HTTP_200_OK

from swagger_ui_bundle import swagger_ui_3_path
import connexion
import prance
# from flask_cors import CORS
from typing import Any, Dict
from pathlib import Path
import os

from libs.database.engine import set_session_destroyer


if os.environ.get('AC_STAGE', '') == 'PRODUCTION':
    import sentry_sdk # 로컬에서 sentry 깔기가 귀찮아서 ㅎㅎ
    from sentry_sdk.integrations.flask import FlaskIntegration
    sentry_sdk.init(
        dsn="https://6981758602ae4a959164cb6cfb7114fe@o390454.ingest.sentry.io/5537977",
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0
    )


app = connexion.App(__name__, specification_dir='api/spec/', options={'swagger_path': swagger_ui_3_path})
set_session_destroyer(app.app)
# CORS(app.app)


def get_bundled_specs(main_file: Path) -> Dict[str, Any]:
    parser = prance.ResolvingParser(str(main_file.absolute()),
                                    lazy = True, strict = True)
    parser.parse()
    return parser.specification


app.add_api(get_bundled_specs(Path("api/spec/main.yaml")),
            resolver = connexion.RestyResolver("cms_rest_api"))



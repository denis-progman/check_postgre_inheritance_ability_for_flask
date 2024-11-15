import os
import pathlib

import requests
import google.auth.transport.requests
from configs import Config, current_config
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from configs import Config
from cachecontrol import CacheControl

class GoogleAuthService:
    USER_PROFILE = "https://www.googleapis.com/auth/userinfo.profile"
    USER_EMAIL = "https://www.googleapis.com/auth/userinfo.email"
    OPENID = "openid"

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = current_config.OAUTHLIB_INSECURE_TRANSPORT
    flow = Flow.from_client_secrets_file(
        client_secrets_file=os.path.join(pathlib.Path(__file__).parent, Config.CLIENT_SECRET_FILE),
        scopes=[USER_PROFILE, USER_EMAIL, OPENID],
        redirect_uri=os.getenv("REDIRECT_URI")
    )

    @staticmethod
    def fetch_token(auth_code):
        __class__.flow.fetch_token(code=auth_code)

    @staticmethod
    def get_google_data(auth_code):
            GoogleAuthService.fetch_token(auth_code)
            id_info = id_token.verify_oauth2_token(
                GoogleAuthService.flow.credentials.id_token,
                google.auth.transport.requests.Request(session=CacheControl(requests.Session())),
                Config.GOOGLE_CLIENT_ID
            )
            return {
                'google_id': id_info["sub"],
                'user_name': id_info["name"],
            }
import os
import pathlib
import requests

from flask import abort, session, request, redirect
from configs import Config

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

from flask import request

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

google_client_id = Config.GOOGLE_CLIENT_ID
client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:8888/callback"
)

def checking():
    # Get the string from the frontend
    data = request.get_json()
    auth_code = data.get('serverAuthCode')
    flow.fetch_token(code=auth_code)

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(
        session=cached_session)

    id_info = id_token.verify_oauth2_token(
        request=token_request,
        audience=google_client_id,
        id_token=credentials._id_token
    )

    google_id = id_info.get("sub")
    user_name = id_info.get("name")
    
    response = {
        'google_id': google_id,
        'user_name': user_name,
        'verification': 'user verified'
    } 
    return response
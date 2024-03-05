import os
import pathlib
import requests

from flask import abort, session, request, redirect, session
from configs import Config
# from flask_oauthlib.client import OAuth

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests


# os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


google_client_id = Config.GOOGLE_CLIENT_ID
client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:8888/callback"
)

def login_window():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

def callback():
    flow.fetch_token(authorization_response=request.url)

    # if not session["state"] == request.args["state"]:
    #     abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(
        session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=google_client_id
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/personal_account")

def personal_account():
    if "google_id" in session:
        return "Logged_in via Google <a href='/log_out'><button>Log out</button></a>"
    else:
        return abort(401) 
    
def account_exit():
    session.clear()
    return redirect("/")
import os
import pathlib
import requests

from controllers.user_controller import UserController

from flask import abort, session, request, redirect
from configs import Config
from services.user_service import UserService
<<<<<<< HEAD
=======
from services.google_auth_service import Google_Auth_Service
from services.apple_auth_service import Apple_Auth_Service
>>>>>>> bb8bfb8 (issue: checking bad request)
# from flask_oauthlib.client import OAuth

from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

from googleapiclient import discovery
from flask import request
import httplib2
from oauth2client import client

<<<<<<< HEAD

=======
>>>>>>> bb8bfb8 (issue: checking bad request)
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

def login_window():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    print(authorization_url)
    print(request.url)
    return redirect(authorization_url)

def callback():
    flow.fetch_token(code=code)

    # if not session["state"] == request.args["state"]:
    #     abort(500)  # State does not match!

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

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/personal_account")

def personal_account():
    if "google_id" in session:       
<<<<<<< HEAD
        UserService.create_user({"google_id":session["google_id"]})
=======
        # existed_user = UserService.get_users_by("google_id", session["google_id"])
        # if not existed_user:
        #     UserService.create_user({"google_id":session["google_id"]})
>>>>>>> bb8bfb8 (issue: checking bad request)
        return "Logged_in via Google <a href='/log_out'><button>Log out</button></a>"
    else:
        return abort(401) 
    
def account_exit():
    session.clear()
    return redirect("/")

def user_auth():
    # (Receive auth_code by HTTPS POST)
    data = request.get_json()

    if data['google_id'] in session:
        return session['key']  #sending the session's key to frontend
    
    auth_code = data['auth_code']

    # If this request does not have `X-Requested-With` header, this could be a CSRF

    if not request.headers.get('X-Requested-With'):
        abort(403)

    # Set path to the Web application client_secret_*.json file you downloaded from the
    # Google API Console: https://console.cloud.google.com/apis/credentials
    CLIENT_SECRET_FILE = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

    # Exchange auth code for access token, refresh token, and ID token
    credentials = client.credentials_from_clientsecrets_and_code(
        CLIENT_SECRET_FILE,
        ['https://www.googleapis.com/auth/drive.appdata', 'profile', 'email'],
        auth_code)
    # Call Google API
    http_auth = credentials.authorize(httplib2.Http())
    drive_service = discovery.build('drive', 'v3', http=http_auth)
    appfolder = drive_service.files().get(fileId='appfolder').execute()

    # Get profile info from ID token
    session['google_id'] = credentials.id_token['sub']
    session['key'] = os.urandom(10).hex()

    if UserController.get_user_by_google_id(session['google_id']):
        return session['key']  #sending the session's key to frontend
    else:
        return redirect("/create_user") 
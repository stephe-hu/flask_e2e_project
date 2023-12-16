from flask import Flask, render_template, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from dotenv import load_dotenv
import os
from db_functions import update_or_create_user
import pandas as pd
from pandas import read_sql
from sqlalchemy import create_engine, inspect
import logging

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/app.log",
    filemode="w",
    format='%(levelname)s - %(name)s - %(message)s'
)

app = Flask(__name__)
app.secret_key = os.urandom(12)
oauth = OAuth(app)
    
# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

@app.route('/')
def index():
    try:
        logging.debug("Success! Index page has been accessed")
        return render_template('index.html')
    except Exception as e:
        logging.error(f"An error occurred! {e}")
        return "Try again"

@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    ###note, if running locally on a non-google shell, do not need to override redirect_uri
    ### and can just use url_for as below
    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    ##, note: if running in google shell, need to override redirect_uri 
    ## to the external web address of the shell, e.g.,
    # redirect_uri = 'https://5000-cs-213132341638-default.cs-us-east1-pkhd.cloudshell.dev/google/auth/'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/data')
def data():
    query_nyc = "SELECT * FROM nyc"
    df_nyc = read_sql(query_nyc, db_engine)
    data_nyc = df_nyc.to_dict(orient='records')
    user = session.get('user')
    return render_template('data.html', data=data_nyc, user=user)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
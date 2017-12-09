# import
import datetime
import dateutil
import dateutil.parser
from flask import Flask, g, url_for, render_template
from sqlalchemy import create_engine

''' INIZIALIZZAZIONE APPLICAZIONE '''

# inizializzo applicazione
app = Flask(__name__)
# config file
app.config.from_envvar('SETTINGS')
# autoreload dei template
app.config['TEMPLATES_AUTO_RELOAD'] = True

''' CONFIGURAZIONE DATABASE '''
def connect_db():
	engine = create_engine(app.config['DATABASE_ELE'], echo=False)
	return engine

def get_db():
	if not hasattr(g, 'postgres'):
		g.postgres = connect_db()
	return g.postgres

@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'postgres'):
		g.postgres.dispose()

''' VISTE '''
from elezioni.views import home
from elezioni.views import facebook
from elezioni.views import twitter
from elezioni.views import news
from elezioni.views import youtube
from elezioni.views import mappe
from elezioni.views import osservatorio

""" UTILS """

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%d %b %Y, %-H:%-M'
    return native.strftime(format)



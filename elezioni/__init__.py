# import
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
from elezioni.views import facebook



# import
from elezioni import app, get_db, render_template, url_for
from flask import jsonify
import json

# first page
@app.route('/')
def home():
    engine = get_db()
    
    cur = engine.execute(
    '''     select
                dt as dt_post
                ,sorgente as sorgente
                ,msg as msg
                ,"user" as utente
            from ''' + app.config['SCHEMA_ELE'] + '''."timeline"
            where dt_rif = (select max(dt_rif) from ''' + app.config['SCHEMA_ELE'] + '''."timeline")
            order by dt desc;
    ''')
    
    timeline = cur.fetchall()
    return render_template('home.html',timeline=timeline)

# contatti
@app.route('/contatti')
def contatti():
    return render_template('contatti.html')

# about
@app.route('/about')
def about():
    return render_template('about.html')
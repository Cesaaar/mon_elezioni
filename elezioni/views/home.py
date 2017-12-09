# import
from elezioni import app, get_db, render_template, url_for
from flask import jsonify, send_from_directory, request
import json

# first page
@app.route('/')
def home():
    engine = get_db()
    
    cur = engine.execute(
    '''     select distinct
                dt as dt_post
                ,sorgente as sorgente
                ,msg as msg
                ,"user" as utente
                ,max(likes) as likes
            from ''' + app.config['SCHEMA_ELE'] + '''."timeline"
            where sorgente != 'news'
            group by dt, sorgente, msg, "user"
            order by dt desc
            limit 20;
    ''')
    
    timeline = cur.fetchall()
    
    id_user1_fb = app.config['USER1_ID_FB']
    id_user2_fb = app.config['USER2_ID_FB']
    id_user3_fb = app.config['USER3_ID_FB']
    
    id_user1_tw = app.config['USER1_ID_TW']
    id_user2_tw = app.config['USER2_ID_TW']
    id_user3_tw = app.config['USER3_ID_TW']
    
    return render_template('home.html',timeline=timeline,id_user1_fb=id_user1_fb,
                           id_user2_fb=id_user2_fb, id_user3_fb=id_user3_fb, id_user1_tw=id_user1_tw,
                           id_user2_tw=id_user2_tw, id_user3_tw=id_user3_tw)

# contatti
@app.route('/contatti')
def contatti():
    return render_template('contatti.html')

# about
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

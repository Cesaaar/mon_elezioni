# import
from elezioni import app, get_db, render_template, url_for
from flask import jsonify, send_from_directory, request, make_response
import json
import os
from datetime import datetime, date, time, timedelta
from jinja2 import Environment, FileSystemLoader

# first page
@app.route('/timeline')
def timeline():
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
    
    return render_template('timeline.html',timeline=timeline,id_user1_fb=id_user1_fb,
                           id_user2_fb=id_user2_fb, id_user3_fb=id_user3_fb, id_user1_tw=id_user1_tw,
                           id_user2_tw=id_user2_tw, id_user3_tw=id_user3_tw)

# contatti
@app.route('/contatti', methods=["GET"])
def contatti():
    return render_template('contatti.html')

# about
@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')

# cookie policy
@app.route('/policy', methods=["GET"])
def policy():
    return render_template('policy.html')

# Generate Sitemap.xml
@app.route('/sitemap.xml', methods=["GET"])
def sitemap():
    """Generate sitemap.xml"""
    pages=[]
    ten_days_ago=(datetime.now() - timedelta(days=10)).date().isoformat()
    
    # dinamic pages
    engine = get_db()
    
    cur = engine.execute(
        '''     select distinct
                    url as url
                    ,"pubAt" as dt_post
                from ''' + app.config['SCHEMA_ELE'] + '''."news"
                order by "pubAt" desc
                limit 1000;
        ''')
    
    news = cur.fetchall()
    for n in news:
        url = n.url
        slashparts = url.split('/')
        final_seg = max(slashparts, key=len)
        end = final_seg.find('.')-1
        final_seg =final_seg[0:end]
        if(len(final_seg)>15):
            base_d = 'http://www.monitoraggioelezioni.it/news/'
            pag_d = base_d+final_seg.replace("&", "-")
            pages.append(
                         [pag_d,ten_days_ago,0.4]
                         )
    
    # static pages
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments)==0:
            base = 'http://www.monitoraggioelezioni.it'
            pag = base+rule.rule
            if(rule.rule=='/'):
                pri = 1
            elif(rule.rule in ('/mappe','/osservatorio','/news')):
                pri = 0.8
            else:
                pri = 0.5
            pages.append(
                        [pag,ten_days_ago,pri]
            )
    # print(pages)
    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response= make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response

@app.route('/robots.txt')
# @app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

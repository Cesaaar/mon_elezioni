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
    
    title = 'Timeline Elezioni Politiche'
    description = '''La timeline social mostra, in ordine cronologico, gli ultimi post Facebook e Twitter dei principali candidati in corsa alle elezioni politiche del 2018'''
    h1 = 'Timeline social delle elezioni politiche italiane'
    current_url = 'www.monitoraggioelezioni.it'+request.path
    
    return render_template('timeline.html',timeline=timeline,id_user1_fb=id_user1_fb,
                           id_user2_fb=id_user2_fb, id_user3_fb=id_user3_fb, id_user1_tw=id_user1_tw,
                           id_user2_tw=id_user2_tw, id_user3_tw=id_user3_tw,
                           title=title, description=description, h1=h1,current_url=current_url)

# contatti
@app.route('/contatti', methods=["GET"])
def contatti():
    title = 'Contatti Elezioni Politiche'
    description = '''Chiarimenti e supporto in relazione al sito di monitoraggio delle elezioni politiche.'''
    h1 = 'Contatti www.monitoraggioelezioni.it'
    current_url = 'www.monitoraggioelezioni.it'+request.path
    return render_template('contatti.html', title=title, description=description, h1=h1,current_url=current_url)

# about
@app.route('/about', methods=["GET"])
def about():
    title = 'About Elezioni Politiche'
    description = '''Monitoraggio del web e dei social dei principali politici italiani, in occasione delle elezioni politiche 2018. Il monitoraggio è apartitico ed è realizzato secondo criteri di trasparenza, sia nella lettura delle fonti che nella sintesi degli indicatori.'''
    h1 = 'About'
    current_url = 'www.monitoraggioelezioni.it'+request.path
    return render_template('about.html',title=title, description=description, h1=h1,
                           current_url=current_url)

# cookie policy
@app.route('/policy', methods=["GET"])
def policy():
    title = 'Policy Estesa'
    description = '''Policy estesa del sito monitoraggio elezioni'''
    h1 = 'Policy Estesa Monitoraggio Elezioni'
    current_url = 'www.monitoraggioelezioni.it'+request.path
    return render_template('policy.html',title=title, description=description, h1=h1,
                           current_url=current_url)

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
    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response= make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response

@app.route('/robots.txt')
# @app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

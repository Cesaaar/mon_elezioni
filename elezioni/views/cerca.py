# coding=utf-8
from elezioni import app, get_db, render_template, url_for
from flask import jsonify, send_from_directory, request, make_response
import json
import os
import re
from datetime import datetime, date, time, timedelta
from jinja2 import Environment, FileSystemLoader

# cerca
@app.route('/cerca', methods = ['POST', 'GET'])
def cerca():
    title = 'Cerca Argomento'
    description = u'''Ricerca gli argomenti trattati dai principali candidati alle elezioni politiche italiane.'''
    h1 = 'Cerca Argomento'
    current_url = 'www.monitoraggioelezioni.it'+request.path
    
    user=request.args.get('user')
    if not user:
        user='Renzi'

    if(request.method == 'POST'):
        result = request.form['text'].lstrip().rstrip()
        result = re.sub(' +',' ',result)
        result = result.replace("'", "''")
        result = result.replace(" ", "&")
        engine = get_db()

        cur = engine.execute(
        '''
            select *
            from (              
              SELECT
              substring(msg from 0 for 100) as titolo
              ,msg as descrizione
              ,cast(max(dt_rif) as text) as data
              ,'http://www.facebook.com/'||id_post as url
              ,"user" as utente
              ,'Facebook' as fonte
              FROM ''' + app.config['SCHEMA_ELE'] + '''."fb_posts"
              WHERE to_tsvector(msg) @@ to_tsquery(''' "'"+result+"'" ''')
              AND "user" = ''' "'"+user+"'" '''
              group by substring(msg from 0 for 100),msg,id_post,"user"
              
              UNION ALL
              
              SELECT
              substring(msg from 0 for 100) as titolo
              ,msg as descrizione
              ,cast(max(dt_rif) as text) as data
              ,'http://www.twitter.com/anyuser/status/'||cast(id_post as text) as url
              ,"user" as utente
              ,'Twitter' as fonte
              FROM ''' + app.config['SCHEMA_ELE'] + '''."tw_posts"
              WHERE to_tsvector(msg) @@ to_tsquery(''' "'"+result+"'" ''')
              AND "user" = ''' "'"+user+"'" '''
              group by substring(msg from 0 for 100),msg,id_post,"user"
          ) a order by data desc
          ''')

        news = cur.fetchall()
        return render_template('cerca.html',result = result,title=title, description=description, h1=h1,
                                   current_url=current_url, news=news, user=user)
    else:
        result=request.args.get('search')
        if not result:
            result=''
            news = []
            return render_template('cerca.html',title=title, description=description, h1=h1,
                                   current_url=current_url,user=user, result=result, news=news)
        else:
            engine = get_db()
            cur = engine.execute(
                             '''
                                 select *
                                 from (
                                 SELECT
                                 substring(msg from 0 for 100) as titolo
                                 ,msg as descrizione
                                 ,cast(max(dt_rif) as text) as data
                                 ,'http://www.facebook.com/'||id_post as url
                                 ,"user" as utente
                                 ,'Facebook' as fonte
                                 FROM ''' + app.config['SCHEMA_ELE'] + '''."fb_posts"
                                     WHERE to_tsvector(msg) @@ to_tsquery(''' "'"+result+"'" ''')
                                         AND "user" = ''' "'"+user+"'" '''
                                             group by substring(msg from 0 for 100),msg,id_post,"user"
                                             
                                             UNION ALL
                                             
                                             SELECT
                                             substring(msg from 0 for 100) as titolo
                                             ,msg as descrizione
                                             ,cast(max(dt_rif) as text) as data
                                             ,'http://www.twitter.com/anyuser/status/'||cast(id_post as text) as url
                                             ,"user" as utente
                                             ,'Twitter' as fonte
                                             FROM ''' + app.config['SCHEMA_ELE'] + '''."tw_posts"
                                                 WHERE to_tsvector(msg) @@ to_tsquery(''' "'"+result+"'" ''')
                                                     AND "user" = ''' "'"+user+"'" '''
                                                         group by substring(msg from 0 for 100),msg,id_post,"user"
                                                         ) a order by data desc
                                                         ''')
        
            news = cur.fetchall()
            return render_template('cerca.html',title=title, description=description, h1=h1,
                           current_url=current_url,user=user, result=result, news=news)

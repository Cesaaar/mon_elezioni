# coding=utf-8
from elezioni import app, get_db, render_template, url_for
from flask import request

# news page
@app.route('/news')
def news():
    engine = get_db()
    
    cur = engine.execute(
    '''     select distinct
                titolo as titolo
                ,"desc" as descrizione
                ,autore as autore
                ,fonte as fonte
                ,url as url
                ,img as img
                ,substring("pubAt" from 12 for 5) as hour_post
                ,to_char(to_date(substring("pubAt" from 0 for 11),'YYYY-MM-DD'), 'DD Month YYYY') as dt_post
                ,max(dt_rif) as dt_rif
                ,max("pubAt") as "pubAt"
            from ''' + app.config['SCHEMA_ELE'] + '''."news"
            group by titolo, "desc",autore, fonte, url, img, substring("pubAt" from 12 for 5),
            to_char(to_date(substring("pubAt" from 0 for 11),'YYYY-MM-DD'), 'DD Month YYYY')
            order by dt_rif desc,"pubAt" desc
            limit 18;
    ''')
    
    news = cur.fetchall()
    
    internal_link = []
    for n in news:
        url = n.url
        slashparts = url.split('/')
        final_seg = max(slashparts, key=len)
        end = final_seg.find('.')-1
        final_seg =final_seg[0:end]
        if(len(final_seg)>15):
            base_d = 'http://www.monitoraggioelezioni.it/news/'
            pag_d = base_d+final_seg.replace("&", "-")
            internal_link.append(pag_d)

    title = 'News Elezioni Politiche Italiane'
    description = u'''Principali news raccolte sul web associate ai candidati alle elezioni politiche oggetto di monitoraggio'''
    h1 = 'News Web'
    current_url = 'www.monitoraggioelezioni.it'+request.path

    return render_template('news.html', news=news, internal_link=internal_link,
                           title=title,description=description,h1=h1,
                           current_url=current_url)

@app.route('/news/<titolo>', methods=['GET'])
def daily_post(titolo):
    engine = get_db()
    cur1 = engine.execute(
    '''     select distinct
                    titolo as titolo
                    ,"desc" as descrizione
                    ,autore as autore
                    ,fonte as fonte
                    ,url as url
                    ,img as img
                    ,substring("pubAt" from 12 for 5) as hour_post
                    ,to_char(to_date(substring("pubAt" from 0 for 11),'YYYY-MM-DD'), 'DD Month YYYY') as dt_post
                    ,max(dt_rif) as dt_rif
                    ,max("pubAt") as "pubAt"
            from ''' + app.config['SCHEMA_ELE'] + '''."news"
            where url ~ '''"'"+titolo+"'"'''
            group by titolo, "desc",autore, fonte, url, img, substring("pubAt" from 12 for 5),
            to_char(to_date(substring("pubAt" from 0 for 11),'YYYY-MM-DD'), 'DD Month YYYY');
    ''')
    
    news_s = cur1.fetchall()
    
    #title = titolo.replace("_", " ")
    #title = title.replace("-", " ")
    title=news_s[0].titolo
    description = u'''Monitoraggio del web e dei social dei principali politici italiani, in occasione delle elezioni politiche 2018. Il monitoraggio è apartitico ed è realizzato secondo criteri di trasparenza, sia nella lettura delle fonti che nella sintesi degli indicatori.'''
    h1 = news_s[0].titolo
    current_url = 'www.monitoraggioelezioni.it'+request.path
    
    return render_template("news_titolo.html",news_s=news_s, title=title, description=description,h1=h1,
                           current_url=current_url)

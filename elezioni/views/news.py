# import
from elezioni import app, get_db, render_template, url_for

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
    
    return render_template('news.html', news=news)

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
    
    return render_template("news_titolo.html",news_s=news_s)

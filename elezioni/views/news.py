# import
from elezioni import app, get_db, render_template, url_for

# news page
@app.route('/news')
def news():
    engine = get_db()
    
    cur = engine.execute(
    '''     select
                titolo as titolo
                ,"desc" as descrizione
                ,autore as autore
                ,fonte as fonte
                ,url as url
                ,img as img
                ,"user" as user
                ,substring("pubAt" from 12 for 5) as hour_post
                ,to_char(to_date(substring("pubAt" from 0 for 11),'YYYY-MM-DD'), 'DD Month YYYY') as dt_post
            from ''' + app.config['SCHEMA_ELE'] + '''."news"
            order by dt_rif desc,"pubAt" desc
            limit 10;
    ''')
    
    news = cur.fetchall()
    
    return render_template('news.html', news=news)

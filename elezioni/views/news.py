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
                ,url as url
                ,img as img
                ,"user" as user
                ,"pubAt" as dt_post
            from ''' + app.config['SCHEMA_ELE'] + '''."news"
            where "user"=''' "'" + app.config['USER1'] + "'" '''
            order by "pubAt" desc
            limit 10;
    ''')
    
    cur2 = engine.execute(
    '''     select
            titolo as titolo
            ,"desc" as descrizione
            ,autore as autore
            ,url as url
            ,img as img
            ,"user" as user
            ,"pubAt" as dt_post
            from ''' + app.config['SCHEMA_ELE'] + '''."news"
            where "user"=''' "'" + app.config['USER2'] + "'" '''
            order by "pubAt" desc
            limit 10;
    ''')
    
    cur3 = engine.execute(
    '''     select
                titolo as titolo
                ,"desc" as descrizione
                ,autore as autore
                ,url as url
                ,img as img
                ,"user" as user
                ,"pubAt" as dt_post
            from ''' + app.config['SCHEMA_ELE'] + '''."news"
            where "user"=''' "'" + app.config['USER3'] + "'" '''
            order by "pubAt" desc
            limit 10;
    ''')
    
    news = cur.fetchall()
    news2 = cur2.fetchall()
    news3 = cur3.fetchall()
    
    return render_template('news.html', news=news, news2=news2, news3=news3)

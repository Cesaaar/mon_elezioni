# import
from elezioni import app, get_db, render_template, url_for
import json

# youtube page
@app.route('/mappe')
def mappe():
    engine = get_db()
    
    cur = engine.execute(
    '''
        SELECT
            provincia
            ,count(*) as menzioni
        FROM ''' + app.config['SCHEMA_ELE'] + '''."mappe"
        WHERE "user"=''' "'" + app.config['USER1'] + "'" '''
        GROUP BY provincia
        ORDER BY count(*) desc
        LIMIT 5;
    ''')
    
    cur2 = engine.execute(
    '''
        SELECT
            provincia
            ,count(*) as menzioni
        FROM ''' + app.config['SCHEMA_ELE'] + '''."mappe"
        WHERE "user"=''' "'" + app.config['USER2'] + "'" '''
        GROUP BY provincia
        ORDER BY count(*) desc
        LIMIT 5;
    ''')
    
    cur3 = engine.execute(
    '''
        SELECT
            provincia
            ,count(*) as menzioni
        FROM ''' + app.config['SCHEMA_ELE'] + '''."mappe"
        WHERE "user"=''' "'" + app.config['USER3'] + "'" '''
        GROUP BY provincia
        ORDER BY count(*) desc
        LIMIT 5;
    ''')
    
    map1 = cur.fetchall()
    map2 = cur2.fetchall()
    map3 = cur3.fetchall()
    
    return render_template('mappe.html',map1=map1, map2=map2, map3=map3)

# json json mappa renzi
@app.route('/mappa_pd')
def mappa_pd():
    engine = get_db()
    cur = engine.execute(
        '''
        select
            count(*) as menzioni
            ,m.provincia
            ,m."user"
            ,max(m.dt_post) as last_dt
            ,max(m.fonte) as fonte
            ,mp.codice as codice
        from ''' + app.config['SCHEMA_ELE'] + '''."mappe" m inner join
            ''' + app.config['SCHEMA_ELE'] + '''."mappe_province" mp on
                m.provincia=mp.nome
        where "user"=''' "'" + app.config['USER1'] + "'" '''
        group by m.provincia, m."user",mp.codice
        order by m."user", m.provincia
        ''')
    
    result = cur.fetchall()
    return json.dumps([dict(r) for r in result])

# json json mappa di maio
@app.route('/mappa_m5s')
def mappa_m5s():
    engine = get_db()
    cur = engine.execute(
    '''
    select
        count(*) as menzioni
        ,m.provincia
        ,m."user"
        ,max(m.dt_post) as last_dt
        ,max(m.fonte) as fonte
        ,mp.codice as codice
    from ''' + app.config['SCHEMA_ELE'] + '''."mappe" m inner join
        ''' + app.config['SCHEMA_ELE'] + '''."mappe_province" mp on
        m.provincia=mp.nome
        where "user"=''' "'" + app.config['USER2'] + "'" '''
        group by m.provincia, m."user",mp.codice
        order by m."user", m.provincia
    ''')
    
    result = cur.fetchall()
    return json.dumps([dict(r) for r in result])

# json json mappa di silvio
@app.route('/mappa_silvio')
def mappa_silvio():
    engine = get_db()
    cur = engine.execute(
                         '''
                             select
                             count(*) as menzioni
                             ,m.provincia
                             ,m."user"
                             ,max(m.dt_post) as last_dt
                             ,max(m.fonte) as fonte
                             ,mp.codice as codice
                             from ''' + app.config['SCHEMA_ELE'] + '''."mappe" m inner join
                                 ''' + app.config['SCHEMA_ELE'] + '''."mappe_province" mp on
                                     m.provincia=mp.nome
                                     where "user"=''' "'" + app.config['USER3'] + "'" '''
                                         group by m.provincia, m."user",mp.codice
                                         order by m."user", m.provincia
                                         ''')
    
    result = cur.fetchall()
    return json.dumps([dict(r) for r in result])

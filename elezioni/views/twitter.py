# import
from elezioni import app, get_db, render_template, url_for
from flask import jsonify
import json

# first page
@app.route('/twitter')
def twitter():
    engine = get_db()
    
    id_user = app.config['USER1_ID_TW']
    id_user2 = app.config['USER2_ID_TW']
    id_user3 = app.config['USER3_ID_TW']
    
    cur = engine.execute(
    '''     select tw_fans
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_fans"
            where "user"=''' "'" + app.config['USER1'] + "'" '''
            order by dt_rif desc
            limit 1;
    ''')
    cur2 = engine.execute(
    '''     select tw_fans
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_fans"
            where "user"=''' "'" + app.config['USER2'] + "'" '''
            order by dt_rif desc
            limit 1;
    ''')
    
    cur3 = engine.execute(
    '''     select tw_fans
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_fans"
            where "user"=''' "'" + app.config['USER3'] + "'" '''
            order by dt_rif desc
            limit 1;
    ''')
    
    cur4 = engine.execute(
    '''     select
            "user" as user_post
            ,to_char(dt_post, 'HH:MM') as hour_post
            ,to_char(dt_post, 'DD Month YYYY') as dt_post2
            ,likes as likes_post
            ,msg as msg_post
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_posts"
            where "user"=''' "'" + app.config['USER1'] + "'" '''
            order by dt_post desc
            limit 1;
    ''')
    
    cur5 = engine.execute(
    '''     select
                "user" as user_post
                ,to_char(dt_post, 'HH:MM') as hour_post
                ,to_char(dt_post, 'DD Month YYYY') as dt_post2
                ,likes as likes_post
                ,msg as msg_post
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_posts"
            where "user"=''' "'" + app.config['USER2'] + "'" '''
            order by dt_post desc
            limit 1;
    ''')
    
    cur6 = engine.execute(
    '''     select
                "user" as user_post
                ,to_char(dt_post, 'HH:MM') as hour_post
                ,to_char(dt_post, 'DD Month YYYY') as dt_post2
                ,likes as likes_post
                ,msg as msg_post
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_posts"
            where "user"=''' "'" + app.config['USER3'] + "'" '''
            order by dt_post desc
            limit 1;
    ''')
    
    tw_fans = cur.fetchall()
    tw_fans2 = cur2.fetchall()
    tw_fans3 = cur3.fetchall()
    
    tw_post = cur4.fetchall()
    tw_post2 = cur5.fetchall()
    tw_post3 = cur6.fetchall()
    
    return render_template('twitter.html',id_user=id_user,id_user2=id_user2, id_user3=id_user3,
                           tw_fans=tw_fans,tw_fans2=tw_fans2,tw_fans3=tw_fans3,
                           tw_post=tw_post, tw_post2=tw_post2, tw_post3=tw_post3)

# json trend tw fans user 1
@app.route('/trend_tw_fans1')
def trend_tw_fans1():
    engine = get_db()
    cur = engine.execute(
        '''
            select
            to_char(dt_rif,'YYYY-MM-DD') as date,
            max(tw_fans) as value
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_fans"
            where "user"=''' "'" + app.config['USER1'] + "'" '''
            group by to_char(dt_rif,'YYYY-MM-DD')
            order by to_char(dt_rif,'YYYY-MM-DD') asc
        ''')
    
    result = cur.fetchall()
    return json.dumps([dict(r) for r in result])

# json trend tw fans user 2
@app.route('/trend_tw_fans2')
def trend_tw_fans2():
    engine = get_db()
    cur = engine.execute(
    '''
        select
            to_char(dt_rif,'YYYY-MM-DD') as date,
            max(tw_fans) as value
        from ''' + app.config['SCHEMA_ELE'] + '''."tw_fans"
        where "user"=''' "'" + app.config['USER2'] + "'" '''
        group by to_char(dt_rif,'YYYY-MM-DD')
        order by to_char(dt_rif,'YYYY-MM-DD') asc
    ''')
    
    result = cur.fetchall()
    return json.dumps([dict(r) for r in result])

# json trend tw fans user 3
@app.route('/trend_tw_fans3')
def trend_tw_fans3():
    engine = get_db()
    cur = engine.execute(
        '''
        select
        to_char(dt_rif,'YYYY-MM-DD') as date,
        max(tw_fans) as value
        from ''' + app.config['SCHEMA_ELE'] + '''."tw_fans"
        where "user"=''' "'" + app.config['USER3'] + "'" '''
        group by to_char(dt_rif,'YYYY-MM-DD')
        order by to_char(dt_rif,'YYYY-MM-DD') asc
    ''')
    
    result = cur.fetchall()
    return json.dumps([dict(r) for r in result])

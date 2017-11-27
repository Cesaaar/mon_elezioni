# import
from elezioni import app, get_db, render_template, url_for
from flask import jsonify
import json

# first page
@app.route('/facebook')
def facebook():
    engine = get_db()
    cur = engine.execute(
    '''     select fb_fans
		from ''' + app.config['SCHEMA_ELE'] + '''."fb_fans"
		where "user"=''' "'" + app.config['USER1'] + "'" '''
		order by dt_rif desc
		limit 1;
            ''')
    cur2 = engine.execute(
    '''      select fb_fans
        	 from ''' + app.config['SCHEMA_ELE'] + '''."fb_fans"
        	 where "user"=''' "'" + app.config['USER2'] + "'" '''
         	order by dt_rif desc
         	limit 1;
     ''')

    cur3 = engine.execute(
    '''      select fb_fans
        	 from ''' + app.config['SCHEMA_ELE'] + '''."fb_fans"
        	 where "user"=''' "'" + app.config['USER3'] + "'" '''
         	order by dt_rif desc
         	limit 1;
     ''')
    
    cur4 = engine.execute(
    '''     select
            "user" as user_post
            ,substring(dt_post from 12 for 5) as hour_post
            ,to_char(to_date(substring(dt_post from 0 for 11),'YYYY-MM-DD'), 'DD Month YYYY') as dt_post2
            ,likes as likes_post
            ,msg as msg_post
            from ''' + app.config['SCHEMA_ELE'] + '''."fb_posts"
            where "user"=''' "'" + app.config['USER1'] + "'" '''
            order by dt_post desc
            limit 1;
    ''')
    
    cur5 = engine.execute(
    '''     select
            "user" as user_post
            ,substring(dt_post from 12 for 5) as hour_post
            ,to_char(to_date(substring(dt_post from 0 for 11),'YYYY-MM-DD'), 'DD Month YYYY') as dt_post2
            ,likes as likes_post
            ,msg as msg_post
            from ''' + app.config['SCHEMA_ELE'] + '''."fb_posts"
            where "user"=''' "'" + app.config['USER2'] + "'" '''
            order by dt_post desc
            limit 1;
    ''')
    
    cur6 = engine.execute(
    '''     select
            "user" as user_post
            ,substring(dt_post from 12 for 5) as hour_post
            ,to_char(to_date(substring(dt_post from 0 for 11),'YYYY-MM-DD'), 'DD Month YYYY') as dt_post2
            ,likes as likes_post
            ,msg as msg_post
            from ''' + app.config['SCHEMA_ELE'] + '''."fb_posts"
            where "user"=''' "'" + app.config['USER3'] + "'" '''
            order by dt_post desc
            limit 1;
    ''')

    fb_fans = cur.fetchall()
    fb_fans2 = cur2.fetchall()
    fb_fans3 = cur3.fetchall()
    
    fb_post = cur4.fetchall()
    fb_post2 = cur5.fetchall()
    fb_post3 = cur6.fetchall()

    id_user = app.config['USER1_ID_FB']
    id_user2 = app.config['USER2_ID_FB']
    id_user3 = app.config['USER3_ID_FB']

    return render_template('facebook.html',fb_fans=fb_fans,fb_fans2=fb_fans2,fb_fans3=fb_fans3,
                           fb_post=fb_post, fb_post2=fb_post2, fb_post3=fb_post3, id_user=id_user,
                           id_user2=id_user2, id_user3=id_user3)


# json trend fb fans user 1
@app.route('/trend_fb_fans1')
def trend_fb_fans1():
    engine = get_db()
    cur = engine.execute(
           '''
               select
                   to_char(dt_rif,'YYYY-MM-DD') as date,
                   fb_fans as value
               from ''' + app.config['SCHEMA_ELE'] + '''."fb_fans"
               where "user"=''' "'" + app.config['USER1'] + "'" '''
               order by dt_rif asc
           ''')

    result = cur.fetchall()
    return json.dumps([dict(r) for r in result])

# json trend fb fans user 2
@app.route('/trend_fb_fans2')
def trend_fb_fans2():
    engine = get_db()
    cur = engine.execute(
    '''
        select
            to_char(dt_rif,'YYYY-MM-DD') as date,
            fb_fans as value
        from ''' + app.config['SCHEMA_ELE'] + '''."fb_fans"
        where "user"=''' "'" + app.config['USER2'] + "'" '''
        order by dt_rif asc
    ''')
        
    result = cur.fetchall()
    return json.dumps([dict(r) for r in result])

# json trend fb fans user 3
@app.route('/trend_fb_fans3')
def trend_fb_fans3():
    engine = get_db()
    cur = engine.execute(
    '''
        select
                to_char(dt_rif,'YYYY-MM-DD') as date,
                fb_fans as value
        from ''' + app.config['SCHEMA_ELE'] + '''."fb_fans"
        where "user"=''' "'" + app.config['USER3'] + "'" '''
        order by dt_rif asc
    ''')
    
    result = cur.fetchall()
    return json.dumps([dict(r) for r in result])


# import
from elezioni import app, get_db, render_template, url_for

# youtube page
@app.route('/osservatorio')
def osservatorio():
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
    
    cur11 = engine.execute(
    '''     select tw_fans
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_fans"
            where "user"=''' "'" + app.config['USER1'] + "'" '''
            order by dt_rif desc
            limit 1;
    ''')
    cur21 = engine.execute(
    '''     select tw_fans
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_fans"
            where "user"=''' "'" + app.config['USER2'] + "'" '''
            order by dt_rif desc
            limit 1;
    ''')
    
    cur31 = engine.execute(
    '''     select tw_fans
            from ''' + app.config['SCHEMA_ELE'] + '''."tw_fans"
            where "user"=''' "'" + app.config['USER3'] + "'" '''
            order by dt_rif desc
            limit 1;
    ''')
    
    cur4 = engine.execute(
    '''     select
                count(id_post)::float/count(distinct dt_post2)::float as post_day
                ,round(sum(likes)/count(distinct dt_post2)) as likes_day
            from(
                select
                    id_post
                    ,max(likes) as likes
                    ,to_date(substring(dt_post from 0 for 11),'YYYY-MM-DD')  as dt_post2
                from ''' + app.config['SCHEMA_ELE'] + '''."fb_posts"
                where "user"=''' "'" + app.config['USER1'] + "'" '''
                group by id_post,to_date(substring(dt_post from 0 for 11),'YYYY-MM-DD')
                ) a;
    ''')
    
    cur5 = engine.execute(
    '''     select
                count(id_post)::float/count(distinct dt_post2)::float as post_day
                ,round(sum(likes)/count(distinct dt_post2)) as likes_day
            from(
                select
                    id_post
                    ,max(likes) as likes
                    ,to_date(substring(dt_post from 0 for 11),'YYYY-MM-DD')  as dt_post2
                from ''' + app.config['SCHEMA_ELE'] + '''."fb_posts"
                where "user"=''' "'" + app.config['USER2'] + "'" '''
                group by id_post,to_date(substring(dt_post from 0 for 11),'YYYY-MM-DD')
                ) a;
    ''')
    
    cur6 = engine.execute(
    '''     select
                count(id_post)::float/count(distinct dt_post2)::float as post_day
                ,round(sum(likes)/count(distinct dt_post2)) as likes_day
                from(
                select
                    id_post
                    ,max(likes) as likes
                    ,to_date(substring(dt_post from 0 for 11),'YYYY-MM-DD')  as dt_post2
                from ''' + app.config['SCHEMA_ELE'] + '''."fb_posts"
                where "user"=''' "'" + app.config['USER3'] + "'" '''
                group by id_post,to_date(substring(dt_post from 0 for 11),'YYYY-MM-DD')
                ) a;
    ''')
    
    cur41 = engine.execute(
    '''     select
                count(id_post)::float/count(distinct dt_post2)::float as post_day
                ,round(sum(likes)/count(distinct dt_post2)) as likes_day
                from(
                    select
                    id_post
                    ,max(likes) as likes
                    ,to_char(dt_post,'YYYY-MM-DD')  as dt_post2
                    from ''' + app.config['SCHEMA_ELE'] + '''."tw_posts"
                    where "user"=''' "'" + app.config['USER1'] + "'" '''
                    group by id_post,to_char(dt_post,'YYYY-MM-DD')
                ) a;
    ''')
    
    cur51 = engine.execute(
    '''     select
                count(id_post)::float/count(distinct dt_post2)::float as post_day
                ,round(sum(likes)/count(distinct dt_post2)) as likes_day
                from(
                    select
                    id_post
                    ,max(likes) as likes
                    ,to_char(dt_post,'YYYY-MM-DD')  as dt_post2
                    from ''' + app.config['SCHEMA_ELE'] + '''."tw_posts"
                    where "user"=''' "'" + app.config['USER2'] + "'" '''
                    group by id_post,to_char(dt_post,'YYYY-MM-DD')
                ) a;
    ''')
    
    cur61 = engine.execute(
    '''     select
                count(id_post)::float/count(distinct dt_post2)::float as post_day
                ,round(sum(likes)/count(distinct dt_post2)) as likes_day
                from(
                    select
                        id_post
                        ,max(likes) as likes
                        ,to_char(dt_post,'YYYY-MM-DD')  as dt_post2
                    from ''' + app.config['SCHEMA_ELE'] + '''."tw_posts"
                    where "user"=''' "'" + app.config['USER3'] + "'" '''
                    group by id_post,to_char(dt_post,'YYYY-MM-DD')
                ) a;
    ''')
    
    id_user1_fb = app.config['USER1_ID_FB']
    id_user2_fb = app.config['USER2_ID_FB']
    id_user3_fb = app.config['USER3_ID_FB']
    
    id_user1_tw = app.config['USER1_ID_TW']
    id_user2_tw = app.config['USER2_ID_TW']
    id_user3_tw = app.config['USER3_ID_TW']
    
    user = []
    user.append(app.config['USER1'])
    user.append(app.config['USER2'])
    user.append(app.config['USER3'])
    
    fb_fans = cur.fetchall()
    fb_fans2 = cur2.fetchall()
    fb_fans3 = cur3.fetchall()
    
    tw_fans = cur11.fetchall()
    tw_fans2 = cur21.fetchall()
    tw_fans3 = cur31.fetchall()
    
    fb_post1 = cur4.fetchall()
    fb_post2 = cur5.fetchall()
    fb_post3 = cur6.fetchall()
    
    tw_post1 = cur41.fetchall()
    tw_post2 = cur51.fetchall()
    tw_post3 = cur61.fetchall()
    
    return render_template('osservatorio.html', fb_fans=fb_fans,fb_fans2=fb_fans2,fb_fans3=fb_fans3,
                           tw_fans=tw_fans,tw_fans2=tw_fans2,tw_fans3=tw_fans3, user=user,
                           id_user1_fb=id_user1_fb, id_user2_fb=id_user2_fb, id_user3_fb=id_user3_fb,
                           id_user1_tw=id_user1_tw,id_user2_tw=id_user2_tw, id_user3_tw=id_user3_tw,
                           fb_post1=fb_post1,fb_post2=fb_post2,fb_post3=fb_post3,
                           tw_post1=tw_post1,tw_post2=tw_post2,tw_post3=tw_post3)
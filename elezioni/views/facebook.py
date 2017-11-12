# import
from elezioni import app, get_db, render_template, url_for

# first page
@app.route('/')
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

    fb_fans = cur.fetchall()
    fb_fans2 = cur2.fetchall()
    fb_fans3 = cur3.fetchall()


    return render_template('facebook.html',fb_fans=fb_fans,fb_fans2=fb_fans2,fb_fans3=fb_fans3)

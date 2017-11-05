# import
from elezioni import app, get_db, render_template, url_for

# first page
@app.route('/')
def facebook():
	engine = get_db()
	cur = engine.execute(
	''' 	select fb_fans 
		from ''' + app.config['SCHEMA_ELE'] + '''."fb_fans"
		where "user"='Renzi'
		order by dt_rif desc
		limit 1;
	''')
	fb_fans = cur.fetchall()
	return render_template('facebook.html',fb_fans=fb_fans)

# import
from elezioni import app, get_db, render_template, url_for

# news page
@app.route('/news')
def news():
    engine = get_db()
    return render_template('news.html')

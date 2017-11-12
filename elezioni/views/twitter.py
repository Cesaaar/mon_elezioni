# import
from elezioni import app, get_db, render_template, url_for

# first page
@app.route('/twitter')
def twitter():
    engine = get_db()
    return render_template('twitter.html')

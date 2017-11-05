# import
from elezioni import app, get_db, render_template, url_for

# first page
@app.route('/')
def facebook():
    return render_template('facebook.html')

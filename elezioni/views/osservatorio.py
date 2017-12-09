# import
from elezioni import app, get_db, render_template, url_for

# youtube page
@app.route('/osservatorio')
def osservatorio():
    engine = get_db()
    return render_template('osservatorio.html')

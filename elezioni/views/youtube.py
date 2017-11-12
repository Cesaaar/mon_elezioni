# import
from elezioni import app, get_db, render_template, url_for

# youtube page
@app.route('/youtube')
def youtube():
    engine = get_db()
    return render_template('youtube.html')

from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import sqlite3

DATABASE = 'objects.db'

app = Flask(__name__)
app.config.from_object(__name__)

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/'
configure_uploads(app, photos)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return render_template('index.html', filename=filename)
    return render_template('index.html')


@app.route('/hello')
def hello():
    gdb = connect_db()
    cur = gdb.execute('select label,features from obj')
    objects = [dict(label=row[0], features=row[1]) for row in cur.fetchall()]
    gdb.close()
    return render_template('hello.html', objects=objects)


if __name__ == "__main__":
    app.run(debug=True)
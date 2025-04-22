#app.py // yes this is called main but its the app

#kinda built this using linux so idk how windows will handle this, i can recommend using windows visual studios just install flask and werkzeug.utils


from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # // 16 MB max // content limit

posts = []

# // check if upload folders exist // maybe?
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.files['image']

        if image:
            filename = secure_filename(image.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(path)

            post = {
                'title': title,
                'description': description,
                'image_url': url_for('static', filename=f'uploads/{filename}')
                }
            posts.insert(0, post) #// for the newest post // it resets

    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)



# // don't mess with the flask code! this code structure is senstive and is a bitch to work with!




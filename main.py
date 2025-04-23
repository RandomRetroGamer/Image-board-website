#app.py // yes this is called main but its the app
#kinda built this using linux so idk how windows will handle this, i can recommend using windows visual studios just install flask and werkzeug.utils

from flask import Flask, render_template, request, redirect, url_for
import os
import json # // adding module <<
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
POSTS_FILE = 'posts.json'

# // functions // load post from files
def load_post():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # falls back if file is corrupted //
    return []

# // saves post files to the files
def save_posts(posts):
    with open(POSTS_FILE, 'w') as f:
        json.dump(posts, f)

# // read file // starter file 
def read_file(file_path):
    try:
        file = open(file_path, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError:
        print(f"Error: file not found at {file_path}")
    finally:
        # // file closes ... 
        if 'file' in locals():
            file.close()

read_file('readme.txt')


# // main route
@app.route('/', methods=['GET', 'POST'])
def index():
    posts = load_post()  # <-- returns loaded from disk

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
                'image': path
            }

            posts.insert(0, post)  # <-- insert the actual post, not the list itself
            save_posts(posts)

        return redirect(url_for('index'))  # // for the newest post // it resets

    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)

#changed the upload folder to keep the images from repeating // changed structure of post append to commit changes faster

# // don't mess with the flask code! this code structure is senstive and is a bitch to work with!

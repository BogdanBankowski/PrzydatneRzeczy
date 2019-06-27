from flask import Flask, render_template, request, redirect
import data_handler
import uuid

app = Flask(__name__)


@app.route('/')
def homepage():
    data = data_handler.get_whole_table()
    return render_template('homepage.html', data=data, DATA_HEADERS=data_handler.DATA_HEADERS)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data_to_add = []
        unique_id = str(uuid.uuid4())[:5]
        data_to_add.append(unique_id)
        for i in range(len(data_handler.DATA_TO_LOAD_FROM_USER)):
            data_to_add.append(request.form[data_handler.DATA_TO_LOAD_FROM_USER[i]])
        data_to_add.append(str(likes[data_to_add[0]]))
        data_handler.add_data_to_file(data_to_add)
        return redirect('/')
    return render_template('add.html', likes=likes)


@app.route('/like/<post_id>')
def like(post_id):
    data_handler.raise_likes_quantity_by_one(post_id)
    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )

from flask import Flask, render_template
import data_handler

app = Flask(__name__)

@app.route('/')
def homepage():
    data = data_handler.get_whole_table()
    return render_template('homepage.html', data=data, DATA_HEADERS = data_handler.DATA_HEADERS)

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == "__main__":
    app.run(
        debug=True, # Allow verbose error reports
        port=5000 # Set custom port
    )
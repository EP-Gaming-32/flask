from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)

def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
#pode ser usado em crud para performar operacoes com base em id
def user(name):
    return render_template('user.html', name = name)

if __name__ == '__main__':
    app.run(debug=True)
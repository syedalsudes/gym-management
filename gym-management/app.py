from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/advantage.html')
def advantage():
    return render_template('advantage.html')

@app.route('/member.html')
def member():
    return render_template('member.html')

@app.route('/trainer.html')
def trainer():
    return render_template('trainer.html')

if __name__ == '__main__':
    app.run(debug=True)

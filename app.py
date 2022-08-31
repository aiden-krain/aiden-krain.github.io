from flask import Flask,render_template,url_for
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Home.html')
@app.route('/recommendation')
def get_recommendation():
    return render_template('recommendation.html')

if __name__ == '__main__':
    app.run(debug=True)
import sys 
from flask import Flask, request, redirect, url_for, render_template

app= Flask(__name__)

@app.route('/',methods=['GET'])
def index_page():
	return render_template("top.html")

@app.route('/goal', methods=['GET'])
def goal_get():
    return render_template("goal.html")

@app.route('/goal', methods=['POST'])
def goal_post():
	goal_text = request.form['goal_text']
	return render_template("goal.html", goal_text=goal_text)

@app.route('/portfolio')
def portfolio():
	return render_template("portfolio.html")

@app.route('/test')
def aaa():
    return render_template("index.html", title="Flaski")

if __name__ == '__main__':
	app.debug = True
	app.run()

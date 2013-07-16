import sys 
from flask import Flask, request, redirect , url_for

app= Flask(__name__)

@app.route('/',methods=['GET'])
def index_page():
	return redirect('./static/top.html')

@app.route('/goal_submit', methods=['POST'])
def goal_page():
	goal_text = request.form['goal_text']
	return "<html><body>%s</body></html>" % goal_text

if __name__ == '__main__':
	app.debug = True
	app.run()
	
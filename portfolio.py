# -*- coding:utf-8 -*-

import sys 
from flask import Flask, request, redirect, url_for, render_template
from pymongo import Connection

app= Flask(__name__)

#コネクション作成
con = Connection('localhost', 27017)

#コネクションからtestデータベースを取得
db = con.test

# 以下のように記載することも可能
# db = con['test']

#testデータベースからfooコレクションを取得
col = db.portfolios

# 以下のように記載することも可能
# col = db['foo']

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


print "========find_one========"
print col.find_one()

print "========find========"
for data in col.find():
    print data

if __name__ == '__main__':
	app.debug = True
	app.run()


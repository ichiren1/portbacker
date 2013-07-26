# -*- coding:utf-8 -*-

import sys 
from flask import Flask, request, redirect, url_for, render_template
from pymongo import Connection

app= Flask(__name__)

#コネクション作成
con = Connection('localhost', 27017)

#コネクションからtestデータベースを取得
db = con.portbacker

# 以下のように記載することも可能
# db = con['test']

#testデータベースからfooコレクションを取得
# col = db.portfolios

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


@app.route('/mongo', methods=['GET'])
def mongo_get():
  #testデータベースからfooコレクションを取得
  col = db.portfolios

  return render_template("mongo.html", col=col)

@app.route('/mongo', methods=['POST'])
def mongo_post():
  col = db.portfolios
  if request.form['button'] == u"設定":
    if request.form['public'] == "true":
      public = True
    else:
      public = False
    owner = request.form['owner']
    text = request.form['text']

    col.insert({"public":public,"owner":owner,"text":text})
  else:
    col.remove({"owner":request.form['owner']})

  
  return render_template("mongo_post.html")

# print "========find_one========"
# print col.find_one()

# print "========find========"
# for data in col.find():
#     print data

if __name__ == '__main__':
	app.debug = True
	app.run()


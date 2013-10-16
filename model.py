#coding: utf-8

from pymongo import Connection

db = Connection('localhost', 27017).portbacker

COL_GOALS = "goals"
COL_PERSONALLOGS = "personallogs"

def get_text_by_user_table_coumn(username, table, column):
    col = db[table]
    docs = col.find({"username": username})
    texts = [doc.get(column) for doc in docs]
    texts = list(filter(None, texts))
    return texts

def get_goal_texts(username):
    goal_texts = get_text_by_user_table_coumn(username, COL_GOALS, "goal_text")
    return goal_texts

def remove_goal_text(username, goal_text):
    col = db[COL_GOALS]
    col.remove({"username": username, "goal_text": goal_text})

def insert_goal_text(username, goal_text):
    col = db[COL_GOALS]
    col.insert({"username": username, "goal_text": goal_text})

def get_log_texts(username):
    log_texts = get_text_by_user_table_coumn(username, COL_PERSONALLOGS, "personallog_text")
    return log_texts

def remove_log_text(username, log_text):
    col = db[COL_PERSONALLOGS]
    col.remove({"username": username, "personallog_text": log_text})

def insert_log_text(username, log_text):
    col = db[COL_PERSONALLOGS]
    col.insert({"username": username, "personallog_text": log_text})


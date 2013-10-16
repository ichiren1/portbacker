#coding: utf-8

from pymongo import Connection

db = Connection('localhost', 27017).portbacker

def get_text_by_user_table_coumn(username, table, column):
    col = db[table]
    docs = col.find({"username": username})
    texts = [doc.get(column) for doc in docs]
    texts = list(filter(None, texts))
    return texts

def get_goal_texts(username):
    goal_texts = get_text_by_user_table_coumn(username, "goals", "goal_text")
    return goal_texts

def remove_goal_text(username, goal_text):
    col = db["goals"]
    col.remove({"username": username, "goal_text": goal_text})

def insert_goal_text(username, goal_text):
    col = db["goals"]
    col.insert({"username": username, "goal_text": goal_text})

def get_log_texts(username):
    log_texts = get_text_by_user_table_coumn(username, "personallogs", "personallog_text")
    return log_texts

def remove_log_text(username, log_text):
    col = db["personallogs"]
    col.remove({"username": username, "personallog_text": log_text})

def insert_log_text(username, log_text):
    col = db["personallogs"]
    col.insert({"username": username, "personallog_text": log_text})


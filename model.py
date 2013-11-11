#coding: utf-8

from pymongo import Connection

class Group(object):
    def __init__(self, name, group_id):
        self.name = name
        self.group_id = group_id
        
    def insert(self, db):
        col = db.portfolio_groups
        col.insert({
            "name": self.name,
            "group_id": self.group_id})
        
            

    @classmethod
    def find(clz , db, group_id):
        col = db.portfolio_groups
        docs = col.find({"group_id": group_id})
        docs = list(docs)
        if len(docs) == 0:
            return None
        doc = docs[0]
        return Group(doc["name"], doc["group_id"])
        
    @classmethod
    def delete_all(clz, db):
        db.drop_collection("portfolio_groups")

class User(object):
    def __init__(self, name, student_id, joining_groups, course, grade):
        self.name = name
        self.student_id = student_id
        self.joining_groups = joining_groups
        self.course = course
        self.grade = grade

    def insert(self, db):
        col = db.portfolio_users
        col.insert({
            "name": self.name,
            "student_id":self.student_id,
            "joining_groups":self.joining_groups,
            "course":self.course,
            "grade":self.grade})

    @classmethod
    def find(clz, db, student_id):
        col = db.portfolio_users
        docs = col.find({"student_id": student_id})
        docs = list(docs)
        if len(docs) == 0:
            return None
        doc = docs[0]
        return User(doc["name"], doc["student_id"], doc["joining_groups"], doc["course"], doc["grade"])

    @classmethod
    def find_user_ids(clz, db):
        col = db.portfolio_users
        docs = col.find()
        store = []
        for doc in docs:
            store.append(doc["student_id"])
        return store

    @classmethod
    def delete_all(clz, db):
        db.drop_collection("portfolio_users")

    @classmethod
    def find_user_ids_by_joining_group(clz, db, group_id):
        col = db.portfolio_users
        docs = col.find()
        store = []
        for doc in docs:
            joining_groups = doc["joining_groups"]
            if group_id in joining_groups:
                store.append(doc["student_id"])
        return store        

class Goal(object):
    def __init__(self, username, title): 
        self.title = title
        self.username = username 

    def insert(self, db):
        col = db.portfolio_goals
        col.insert({
            "title": self.title,
            "username": self.username})

    @classmethod
    def find(clz , db, username, title):
        col = db.portfolio_goals
        docs = col.find({"title": title, "username": username})
        docs = list(docs)
        if len(docs) == 0:
            return None
        doc = docs[0]
        return Goal(doc["title"], doc["username"])

    @classmethod
    def delete_all(clz, db):
        db.drop_collection("portfolio_goals")

class GoalItem(object):
    def __init__(self, username, link_to_goal, title, change_data,visibility):
        self.title = title
        self.username = username
        self.change_data = change_data 
        self.link_to_goal = link_to_goal
        self.visibility = visibility


    def insert(self, db):
        col = db.portfolio_goalitems
        col.insert({
            "title": self.title,
            "username": self.username,
            "change_data": self.change_data,
            "link_to_goal": self.link_to_goal,
            "visibility": self.visibility})

    @classmethod
    def find(clz , db, username , link_to_goal, title):
        col = db.portfolio_goalitems
        docs = col.find({
            "title": title,
            "link_to_goal": link_to_goal,
            "username" : username})
        docs = list(docs)
        if len(docs) == 0:
            return None
        doc = docs[0]
        return GoalItem(doc["title"], doc["username"],doc["change_data"], doc["link_to_goal"], doc["visibility"])

    @classmethod
    def delete_all(clz, db):
        db.drop_collection("portfolio_goalitems")

db = Connection('localhost', 27017).portbacker

COL_GOALS = "goals"
COL_PERSONALLOGS = "personallogs"

def get_text_by_user_table_coumn(username, table, column):
    col = db[table]
    docs = col.find({"username": username})
    texts = [doc.get(column) for doc in docs]
    texts = list(filter(None, texts))
    return texts

def get_goaltexts(username):
    goaltexts = get_text_by_user_table_coumn(username, COL_GOALS, "goal_text")
    ObjectIDs = get_text_by_user_table_coumn(username, COL_GOALS, "ObjectID") # ichirenadd
    return goaltexts, ObjectIDs

def remove_goaltext(username, _id):
    col = db[COL_GOALS]
    col.remove({"username": username, "ObjectID": _id })

def insert_goaltext(username, goaltext):
    col = db[COL_GOALS]
    col.insert({"username": username, "goal_text": goaltext})

def get_log_texts(username):
    log_texts = get_text_by_user_table_coumn(username, COL_PERSONALLOGS, "personallog_text")
    return log_texts

def remove_log_text(username, log_text):
    col = db[COL_PERSONALLOGS]
    col.remove({"username": username, "personallog_text": log_text})

def insert_log_text(username, log_text):
    col = db[COL_PERSONALLOGS]
    col.insert({"username": username, "personallog_text": log_text})


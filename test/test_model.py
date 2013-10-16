#coding: utf-8

import unittest
from pymongo import Connection

import model


class ModelTest(unittest.TestCase):
    def setUp(self):
        db = Connection('localhost', 27017).testdata
        model.db = db
        db[model.COL_GOALS].drop()
        db[model.COL_PERSONALLOGS].drop()

    def test_insert_goal_text(self):
        u = "morohara"
        gt = u"PHPマスターする"

        goal_texts = model.get_goal_texts(u)
        self.assertFalse(gt in goal_texts)

        model.insert_goal_text(u, gt)
        goal_texts = model.get_goal_texts(u)
        self.assertTrue(gt in goal_texts)

    def test_remove_goal_text(self):
        u = "morohara"
        gt = u"PHPマスターする"

        model.insert_goal_text(u, gt)
        goal_texts = model.get_goal_texts(u)
        self.assertTrue(gt in goal_texts)

        model.remove_goal_text(u, gt)
        goal_texts = model.get_goal_texts(u)
        self.assertFalse(gt in goal_texts)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
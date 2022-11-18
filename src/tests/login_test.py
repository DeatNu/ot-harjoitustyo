import unittest
import sys
import os
import random 
import string
parent_dir = os.path.abspath(__file__ + "/../../")
sys.path.append(parent_dir)
import login

class TestInit(unittest.TestCase):
    def setUp(self):
        parent_dir = os.path.abspath(__file__ + "/../../")
        parent_parent = os.path.abspath(__file__ + "/../../../")
        sys.path.append(parent_dir)
        self.db_path = parent_parent + "/users.db"
        self.db_path_opt = parent_dir + "/users.db"
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_database_created(self):
        db = login.init()
        self.assertEqual(str(type(db)),"<class 'sqlite3.Connection'>")
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_add_users(self):
        db = login.init()
        names = self.create_names()
        login.add_users(db, names[0],names[1])
        retrieved = db.execute("SELECT name FROM Users").fetchall()
        self.assertEqual([name[0] for name in retrieved], names)
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass


    def create_names(self):
        length = random.randint(2,20)
        names = []
        for i in range(2):
            name = ""
            for j in range(length):
                name += random.choice(string.printable[0:93])
            names.append(name)
        return names

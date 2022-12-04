#import login
import unittest
import sys
import os
import random
import string
from db import login


class TestInit(unittest.TestCase):
    def setUp(self):
        parent_dir = os.path.abspath(__file__ + "/../../")
        parent_parent = os.path.abspath(__file__ + "/../../../")
        sys.path.append(parent_dir)
        self.db_path = parent_parent + "/pyshare.db"
        self.db_path_opt = parent_dir + "/pyshare.db"
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_database_created(self):
        db = login.init()
        self.assertEqual(str(type(db)), "<class 'sqlite3.Connection'>")
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_add_users(self):
        db = login.init()
        names = self.create_names()
        login.add_users(db, names[0], names[1])
        retrieved = db.execute("SELECT name FROM Users").fetchall()
        self.assertEqual([name[0] for name in retrieved], names)
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def create_names(self):
        length = random.randint(2, 20)
        names = []
        for i in range(2):
            name = ""
            for j in range(length):
                name += random.choice(string.printable[0:93])
            names.append(name)
        return names

    def test_fetch_names(self):
        db = login.init()
        names = self.create_names()
        login.add_users(db, names[0], names[1])
        name1, name2 = login.fetch_names()
        self.assertEqual((name1, name2), (names[0], names[1]))
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_validate_name(self):
        db = login.init()
        names = self.create_names()
        login.add_users(db, names[0], names[1])
        response1 = login.validate_name(names[0])
        response2 = login.validate_name(names[1])
        response3 = login.validate_name("wrong_user")
        self.assertListEqual([response1, response2, response3], [
                             True, True, False])
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

import access
import login
import unittest
import sys
import os
parent_dir = os.path.abspath(__file__ + "/../../")
sys.path.append(parent_dir)


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
        db = login.init()
        login.add_users(db, "test_user1", "test_user2")

    def test_init(self):
        db = access.init()
        db = access.init()
        self.assertEqual(str(type(db)), "<class 'sqlite3.Connection'>")
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_pay(self):
        db = access.init()
        self.assertEqual(access.pay(db, "test_user1", 10, 56), True)
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_get_sum(self):
        db = access.init()
        access.pay(db, "test_user1", 40, 23)
        self.assertEqual(access.get_sum(db, "test_user1"), 23.0)
        access.pay(db, "test_user1", 5, 10)
        self.assertEqual(access.get_sum(db, "test_user1"), 33.0)
        access.pay(db, "test_user2", 0, 33)
        self.assertEqual(access.get_sum(db, "test_user1"), 0.0)
        self.assertEqual(access.get_sum(db, "test_user2"), 0.0)
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

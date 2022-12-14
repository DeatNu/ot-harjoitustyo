import unittest
import sys
import os
from db import access
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
        db = login.init()
        login.add_users(db, ["test_user1", "test_pwd1,",
                        "test_user2", "test_pwd2"])

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
        comment = "groceries"
        self.assertEqual(access.pay(db, "test_user1", 10, 56, comment), True)
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_get_sum(self):
        db = access.init()
        comment = ""
        access.pay(db, "test_user1", 40, 23, comment)
        self.assertEqual(access.get_sum(db, "test_user1")[0], 23.0, comment)
        self.assertEqual(access.get_sum(db, "test_user1")[1], "green")
        self.assertEqual(access.get_sum(db, "test_user2")[1], "red")
        access.pay(db, "test_user1", 5, 10, comment)
        self.assertEqual(access.get_sum(db, "test_user1")[0], 33.0)
        self.assertEqual(access.get_sum(db, "test_user1")[1], "green")
        self.assertEqual(access.get_sum(db, "test_user2")[1], "red")
        access.pay(db, "test_user2", 0, 33, comment)
        self.assertEqual(access.get_sum(db, "test_user1")[0], 0.0)
        self.assertEqual(access.get_sum(db, "test_user2")[0], 0.0)
        self.assertEqual(access.get_sum(db, "test_user1")[1], "black")
        access.pay(db, "test_user1", 10, 10, comment)
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_transactions(self):
        db = access.init()
        comment = ""
        access.pay(db, "test_user1", 100, 10, comment)
        access.pay(db, "test_user1", 5, 10, comment)
        access.pay(db, "test_user2", 0, 33, comment)
        access.pay(db, "test_user2", 40, 40, comment)
        data = access.get_transactions(db)
        self.assertEqual(data, [("test_user1", 100.0, 10.0, ""), ("test_user1",
                         5.0, 10.0, ""), ("test_user2", 0.0, 33.0, ""), ("test_user2", 40.0, 40.0, "")])
        print(data)
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_convert_names(self):
        user1 = "test_12"
        other1 = "test_45"
        name1, name2 = access.convert_names(user1, [user1, other1])
        self.assertEqual((name1, name2), (user1+"'s", other1+"'s"))
        user1 = "test_56"
        other1 = "test_14"
        name1, name2 = access.convert_names(user1, [other1, user1])
        self.assertEqual((name1, name2), (user1+"'s", other1+"'s"))
        user1 = "Jonas"
        other1 = "Jacks"
        name1, name2 = access.convert_names(user1, [user1, other1])
        self.assertEqual((name1, name2), (user1+"'", other1+"'"))
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_pay_invalid(self):
        db = access.init()
        user = "test_user1"
        comment = ""
        shares = [(-1, 1), (1, -1), ("f", 1), ("", 4), (56, ""), (1, "67f")]
        for share in shares:
            response = access.pay(db, user, share[0], share[1], "")
            self.assertEqual(response, False)
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_get_sum_large_number(self):
        db = access.init()
        comment = ""
        access.pay(db, "test_user1", 1, 230_000_000_000, comment)
        self.assertEqual(access.get_sum(db, "test_user1")[0], "2.30E+11")
        db = access.init()
        access.pay(db, "test_user1", 1, 240_000_000_000, comment)
        self.assertEqual(access.get_sum(db, "test_user1")[0], "4.70E+11")
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_get_sum_invalid(self):
        db = access.init()
        comment = ""
        access.pay(db, "test_user1", 1, 230_000_000_000, comment)
        self.assertEqual(access.get_sum(db, "test_user11")[0], "0", "black")
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass
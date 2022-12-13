#import login
import unittest
import sys
import os
import random
import string
from db import login
import bcrypt


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
        names = self.create_names_and_pwds()
        login.add_users(db, names)
        retrieved = db.execute("SELECT name FROM Users").fetchall()
        self.assertEqual([name[0] for name in retrieved], names[::2])
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def create_names_and_pwds(self):
        length = random.randint(2, 20)
        names = []
        for i in range(4):
            name = ""
            for j in range(length):
                name += random.choice(string.printable[0:93])
            names.append(name)
        return names

    def test_fetch_names(self):
        db = login.init()
        names = self.create_names_and_pwds()
        login.add_users(db, names)
        name1, name2 = login.fetch_names()
        self.assertEqual((name1, name2), (names[0], names[2]))
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_validate_name(self):
        db = login.init()
        names = self.create_names_and_pwds()
        login.add_users(db, names)
        response1 = login.validate_name(names[0])
        response2 = login.validate_name(names[2])
        response3 = login.validate_name("wrong_user")
        self.assertListEqual([response1, response2, response3], [
                             True, True, False])
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_hash(self):
        salt = bytes(
            "$2b$13$HBtqy0fx3TqYE8/GUYqbK.stmFtRJbh6.dfSg9s/g83hf/2hfksf1", encoding='utf-8')
        pwd = "testi_pwd"
        pwd_h = bytes(pwd, encoding="utf-8")
        hashed = login.hash_pwd(pwd, salt)
        self.longMessage = True
        self.assertEqual(hashed, (bcrypt.hashpw(pwd_h, salt), salt))
        hashed2, s = login.hash_pwd(pwd)
        self.assertCountEqual(hashed2, bcrypt.hashpw(pwd_h, s), s)
        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

    def test_validate_pwd(self):
        db = login.init()
        names = self.create_names_and_pwds()
        fake_names = self.create_names_and_pwds()
        login.add_users(db, names)
        response = login.validate_pwd(names[0:2])
        response2 = login.validate_pwd(names[2:4])
        response3 = login.validate_pwd(fake_names[0:2])
        response4 = login.validate_pwd(fake_names[2:4])
        self.assertEqual(response, True)
        self.assertEqual(response2, True)
        self.assertEqual(response3, False)
        self.assertEqual(response4, False)

        try:
            os.remove(self.db_path)
            os.remove(self.db_path_opt)
        except FileNotFoundError:
            pass

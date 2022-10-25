import unittest
class TestStringMethods(unittest.TestCase):   
    def setUp(self):
        pass
    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        self.assertEqual( 'a'*4, 'aaaa')
    # Returns True if the string is in upper case.
    def test_upper(self):        
        self.assertEqual('foo'.upper(), 'FOO')
    # Returns TRUE if the string is in uppercase else returns False.
    def test_isupper(self):        
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    # Returns true if the string is stripped and matches the given output.
    def test_strip(self):        
        s = 'This is a Testcode'
        self.assertEqual(s.strip('This is '), 'a Testcode')
    # Returns true if the string splits and matches the given output.
    def test_split(self):        
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
if __name__ == '__main__':
    unittest.main()

###################################################
class User:
    def __init__(self):
        self.profile = {'active':False,'level':1,'points':0}
    def activate(self):
        self.profile['active'] = True
    def is_active(self):
        return self.profile['active']
    def get_level(self):
        return self.profile['level']
    def get_points(self):
        return self.profile['points']
    def add_points(self, additional_points):
        self.profile['points'] += additional_points
        if self.get_points() > 300:
            self.profile['level'] = 3
        elif self.get_points() > 200:
            self.profile['level'] = 2
#create an object
user1 = User()
print(user1.__dict__)

#################################################

class User:
    def __init__(self):
        self.profile={'active':False,'level':1,'points':0}
    def activate(self):
        self.profile['active'] = True
    def is_active(self):
        return self.profile['active']
    def get_level(self):
        return self.profile['level']
    def get_points(self):
        return self.profile['points']
    def add_points(self, additional_points):
        self.profile['points'] += additional_points
        if self.get_points() > 300:
            self.profile['level'] = 3
        elif self.get_points() > 200:
            self.profile['level'] = 2
#create an object
user1 = User()
print(user1.__dict__)


##############################################
class User:
    def __init__(self):
        self.profile={'active':False,'level':1,'points':0}
        
    def activate(self):
        self.profile['active'] = True
    def is_active(self):
        return self.profile['active']
    def get_level(self):
        return self.profile['level']
    def get_points(self):
        return self.profile['points']
    def add_points(self, additional_points):
        self.profile['points'] += additional_points
        if self.get_points() > 300:
            self.profile['level'] = 3
        elif self.get_points() > 200:
            self.profile['level'] = 2
##################################################
import unittest
class TestUser(unittest.TestCase):
    def test_user_activation(self):
        user1 = User()
        user1.activate()
        self.assertTrue(user1.is_active())
    def test_user_points_update(self):
        user1 = User()
        user1.add_points(25)
        self.assertEqual(user1.get_points(), 25)

    def test_user_level_change(self):
        user1 = User()
        user1.add_points(205)
        self.assertEqual(user1.get_level(), 2)
if __name__ == '__main__':
    unittest.main()

###################################################
class User:
    def __init__(self):
        self.profile = {'active': False,'level':1,'points':0}
        
    def activate(self):
        self.profile['active'] = True
    def is_active(self):
        return self.profile['active_user']
    def get_level(self):
        return self.profile['level']
    def get_points(self):
        return self.profile['points']
    def add_points(self, additional_points):
        self.profile['points'] += additional_points
        if self.get_points() > 300:
            self.profile['level'] = 3
        elif self.get_points() > 200:
            self.profile['level'] = 2

##################################################
import unittest
class TestUser(unittest.TestCase):
    def test_user_activation(self):
        user1 = User()
        user1.activate()
        self.assertTrue(user1.is_active())
if __name__ == '__main__':
    unittest.main()




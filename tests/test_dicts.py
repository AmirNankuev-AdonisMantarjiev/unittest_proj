import unittest
from utils.dicts import get_val


class TestGetVal(unittest.TestCase):

    def test_key_exists_no_default_needed(self):
        collection = {"vcs": "mercurial", "language": "python"}
        self.assertEqual(get_val(collection, "vcs"), "mercurial")
        self.assertEqual(get_val(collection, "language"), "python")

    def test_key_exists_default_provided(self):
        data = {"vcs": "mercurial"}
        self.assertEqual(get_val(data, "vcs", "git"), "mercurial")
        self.assertEqual(get_val(data, "vcs", "bazaar"), "mercurial")

    def test_key_not_exists_returns_default(self):
        self.assertEqual(get_val({}, "vcs", "git"), "git")
        self.assertEqual(get_val({}, "vcs", "bazaar"), "bazaar")

        data = {"name": "John", "age": 25}
        self.assertEqual(get_val(data, "city", "Unknown"), "Unknown")
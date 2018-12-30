import unittest
import vault

class TestVault(unittest.TestCase):

    def test_check_url(self):
        self.assertEqual(vault.check_url("http://url"), "http://url")
        self.assertEqual(vault.check_url("url"), "http://url")

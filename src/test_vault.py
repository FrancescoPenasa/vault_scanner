import unittest
import vault

#python3 -m unittest --verbose test_vault.py
#BLACKBOX TESTING

class TestVault(unittest.TestCase):
    def test_check_url(self):
        self.assertEqual(vault.check_url("http://url"), "http://url")
        self.assertEqual(vault.check_url("url"), "http://url")

    def test_check_ip(self):
        self.assertEqual(vault.check_ip("255.255.255.255"), "255.255.255.255")
        self.assertEqual(vault.check_ip("0.0.0.0"), "0.0.0.0")
        #self.assertEqual(vault.check_ip("000.000.000.000"), "000.000.000.000")
        #self.assertEqual(vault.check_ip("00.00.00.00"), "00.00.00.00")

    
class ExpectedFailureTestCase(unittest.TestCase):

    ### TESTS check_ip(url:str) ###
    @unittest.expectedFailure
    def test_fail_check_ip_lower_boundaries_1(self):
        self.assertEqual(vault.check_ip("0.0.0.-1"), "0.0.0.-1")
    @unittest.expectedFailure
    def test_fail_check_ip_lower_boundaries_2(self):
        self.assertEqual(vault.check_ip("0.0.-1.0"), "0.0.-1.0")
    @unittest.expectedFailure
    def test_fail_check_ip_lower_boundaries_3(self):
        self.assertEqual(vault.check_ip("0.-1.0.0"), "0.-1.0.0")
    @unittest.expectedFailure
    def test_fail_check_ip_lower_boundaries_4(self):
        self.assertEqual(vault.check_ip("-1.0.0.0"), "-1.0.0.0")
    @unittest.expectedFailure
    def test_fail_check_ip_upper_boundaries_1(self):
        self.assertEqual(vault.check_ip("0.0.0.256"), "0.0.0.256")
    @unittest.expectedFailure
    def test_fail_check_ip_upper_boundaries_2(self):
        self.assertEqual(vault.check_ip("0.0.256.0"), "0.0.256.0")
    @unittest.expectedFailure
    def test_fail_check_ip_upper_boundaries_3(self):
        self.assertEqual(vault.check_ip("0.256.0.0"), "0.256.0.0")
    @unittest.expectedFailure
    def test_fail_check_ip_upper_boundaries_4(self):
        self.assertEqual(vault.check_ip("256.0.0.0"), "256.0.0.0")

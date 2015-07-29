'''
Created on Jul 29, 2015

@author: ronaldjosephdesmarais
'''
import unittest
import ATPC

class Test(unittest.TestCase):

    def setUp(self):
        self.conv=ATPC
        pass


    def tearDown(self):
        conv=None
        pass


    def testAscToPetString(self):
        send_test_msg="hi there is a dog over there"
        trans_msg="HI THERE IS A DOG OVER THERE"
        result= self.conv.asc_to_pet_s(send_test_msg,result_type='string')
        self.assertEqual(result, trans_msg, "Message %s not as exprected %s"%(result,trans_msg))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
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
        self.conv=None
        pass


    def testAscToPetStringToString(self):
        send_test_msg="hi there is a dog over there"
        trans_msg="HI THERE IS A DOG OVER THERE"
        result= self.conv.asc_to_pet_s(send_test_msg,result_type='string')
        self.assertEqual(result, trans_msg, "Message %s not as expected %s"%(result,trans_msg))
        pass
    
    #this test case sends all capitals ... which translates to petscii very nicely in either upper or lower case (depends on C64 shift mode)
    def testPetToAscStringToString(self):
        send_test_msg="HI THERE IS A DOG OVER THERE"
        trans_msg="hi there is a dog over there"
        result= self.conv.pet_to_asc_s(send_test_msg,result_type='string')
        #print result
        self.assertEqual(result, trans_msg, "Message %s not as expected %s"%(result,trans_msg))
        pass
    
    #this test case can only test the return bytes since a return string in petscii is very high in the ascii table
    def testPetToAscStringToBytes(self):
        send_test_msg="hi there is a dog over there"
        trans_msg=[200, 201, 32, 212, 200, 197, 210, 197, 32, 201, 211, 32, 193, 32, 196, 207, 199, 32, 207, 214, 197, 210, 32, 212, 200, 197, 210, 197]
        result= self.conv.pet_to_asc_s(send_test_msg,result_type='default')
        #print result
        self.assertEqual(result, trans_msg, "Message %s not as expected %s"%(result,trans_msg))
        pass
    
    #this test case can only test the return bytes since a return string in ascii is very high in the ascii table
    def testAscToPetStringToBytes(self):
        send_test_msg="hi there is a dog over there"
        trans_msg=[72, 73, 32, 84, 72, 69, 82, 69, 32, 73, 83, 32, 65, 32, 68, 79, 71, 32, 79, 86, 69, 82, 32, 84, 72, 69, 82, 69]
        result= self.conv.asc_to_pet_s(send_test_msg,result_type='default')
        #print result
        self.assertEqual(result, trans_msg, "Message %s not as expected %s"%(result,trans_msg))
        pass
    
    def testAscToPetByteToByte(self):
        send_test_msg_bytes=self.conv.get_bytes("hi there is a dog over there")
        trans_msg=[72, 73, 32, 84, 72, 69, 82, 69, 32, 73, 83, 32, 65, 32, 68, 79, 71, 32, 79, 86, 69, 82, 32, 84, 72, 69, 82, 69]
        result= self.conv.asc_to_pet_b_arr(send_test_msg_bytes,result_type='default')
        self.assertEqual(result, trans_msg, "Message %s not as expected %s"%(result,trans_msg))
        pass
    
    #this test case sends all capitals ... which translates to petscii very nicely in either upper or lower case (depends on C64 shift mode)
    def testPetToAscByteToByte(self):
        send_test_msg=self.conv.get_bytes("HI THERE IS A DOG OVER THERE")
        trans_msg=[104, 105, 32, 116, 104, 101, 114, 101, 32, 105, 115, 32, 97, 32, 100, 111, 103, 32, 111, 118, 101, 114, 32, 116, 104, 101, 114, 101]
        result= self.conv.pet_to_asc_b_arr(send_test_msg,result_type='default')
        #print result
        self.assertEqual(result, trans_msg, "Message %s not as expected %s"%(result,trans_msg))
        pass
    
    def testAscToPetByteToString(self):
        send_test_msg_bytes=self.conv.get_bytes("hi there is a dog over there")
        trans_msg="HI THERE IS A DOG OVER THERE"
        result= self.conv.asc_to_pet_b_arr(send_test_msg_bytes,result_type='string')
        self.assertEqual(result, trans_msg, "Message %s not as expected %s"%(result,trans_msg))
        pass
    
    #this test case sends all capitals ... which translates to petscii very nicely in either upper or lower case (depends on C64 shift mode)
    def testPetToAscByteToString(self):
        send_test_msg=self.conv.get_bytes("HI THERE IS A DOG OVER THERE")
        trans_msg="hi there is a dog over there"
        result= self.conv.pet_to_asc_b_arr(send_test_msg,result_type='string')
        #print result
        self.assertEqual(result, trans_msg, "Message %s not as expected %s"%(result,trans_msg))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
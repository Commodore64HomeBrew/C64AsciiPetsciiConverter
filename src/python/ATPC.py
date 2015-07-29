"""
Created on Jul 28, 2015

@author: andi bergen

Purpose: Convert single character of ASCII to PETSCII and vice versa.
         Also converts string of ASCII to list of hex PETSCII values.
"""

import tables
import logging

logging.basicConfig(filename='conv.log',level=logging.DEBUG)

def pet_to_asc_b_arr(in_bytes,result_type='default'):
    """
    Purpose: converts PETSCII bytes to ASCII
    Input: array of bytes
    Output: returns hex array of ASCII bytes or a string (ascii) representation of bytes
    """
    ret = []
    ret_str=''
    for b in in_bytes:
        ret.append(pet_to_asc_b(b))
        ret_str="%s%s"%(ret_str,chr(pet_to_asc_b(b)))
    if result_type == 'default':
        return ret
    else:
        return ret_str


def pet_to_asc_b(in_byte):
    """
    Purpose: converts PETSCII byte/unicode to ASCII
    Input: single byte/hex value
    Output: returns hex value of ASCII character
    """
    ret = tables.petToAscTable[in_byte]
    logging.debug("petscii byte: %s to %s"%(in_byte,ret))
    return ret

def asc_to_pet_b_arr(in_bytes,result_type='default'):
    """
    Purpose: converts ASCII bytes to PETSCII
    Input: array of bytes
    Output: returns hex array of PETSCII bytes or a string (which will be in ascii rep. but petscii byte) representation of bytes
    """
    ret = []
    ret_str=''
    for b in in_bytes:
        ret.append(asc_to_pet_b(b))
        ret_str="%s%s"%(ret_str,chr(asc_to_pet_b(b)))
    if result_type == 'default':
        return ret
    else:
        return ret_str


def asc_to_pet_b(in_byte):
    """
    Purpose: converts PETSCII byte/unicode to ASCII
    Input: single byte/hex value
    Output: returns hex value of ASCII character
    """
    ret = tables.ascToPetTable[in_byte]
    logging.debug("ascii byte: %s to %s"%(in_byte,ret))
    return ret
    
def pet_to_asc_c(in_char):
    """
    Purpose: converts PETSCII character to ASCII
    Input: single character/hex value
    Output: returns hex value of ASCII character
    """
    
    logging.debug("in petToAscC %s "%in_char)
    
    if len(in_char) != 1:
        logging.warning("in pet_to_asc_c")
        logging.warning("you are calling the wrong function")
        logging.warning("parameter should be a single character")
        return -1
    ret = tables.petToAscTable[ord(in_char)]
    logging.debug("pet character: " + str(ord(in_char)) + " to " + str(chr(ret)))
    return ret


def pet_to_asc_s(in_str,result_type='default'):
    """
    Purpose: converts PETSCII string to ASCII
    Input: PETSCII string
    Output: returns list of hex values of ASCII characters or an Ascii String representation
    """
    # not sure if you need this or what you'd pass in
    logging.debug("in pet_to_asc_s "+str(in_str))
    ret = []
    ret_str=''
    for in_char in in_str:
        ret.append(pet_to_asc_c(in_char))
        ret_str="%s%s"%(ret_str,chr(pet_to_asc_c(in_char)))
    if result_type == 'default':
        return ret
    else:
        return ret_str


def asc_to_pet_c(in_char):
    """
    Purpose: converts ASCII character to PETSCII
    Input: single character/hex value
    Output: returns hex value of PETSCII character
    """
    logging.debug("in asc_to_pet_c")
    if len(in_char) != 1:
        logging.warning("in asc_to_pet_c")
        logging.warning("you are calling the wrong function")
        logging.warning("parameter should be a single character")
        return -1
    ret = tables.ascToPetTable[ord(in_char)]
    logging.debug("ascii character: " + str(in_char) + " to " + str(ret))
    return ret


def asc_to_pet_s(in_str,result_type='default'):
    """
    Purpose: converts ASCII string to list of PETSCII hex values
    Input: ASCII string
    Output: returns list of hex values of PETSCII characters or an Ascii String representation
    """
    logging.debug("in asc_to_pet_s")
    ret = []
    ret_str=''
    for in_char in in_str:
        ret.append(asc_to_pet_c(in_char))
        ret_str="%s%s"%(ret_str,chr(asc_to_pet_c(in_char)))
    if result_type == 'default':
        return ret
    else:
        return ret_str
    
#some other utilities
def get_bytes(msg_str):
    return [ord(elem) for elem in msg_str]

def examples():
    """
    Purpose: runs through some simple examples
    Input: nothing
    Output: Side effect is that things are printed to the screen
    """
    logging.info("Lets Run some Test cases")
    print("\n\nKEEP IN MIND THAT THE RETURN VALUE IS JUST AN INTEGER")
    print("")
    print("String 'HI THERE A' to petscii: " + str(asc_to_pet_s("HI THERE A")))
    print("String 'hi there a' to petscii: " + str(asc_to_pet_s("hi there a")))
    print ("Seems Wrong, but its actually correct since input is actually in ascii, not petscii")
    print("String 'HI THERE A' to ascii: " +  str(pet_to_asc_s('HI THERE A')))
    print("String 'hi there a' to ascii: " +  str(pet_to_asc_s('hi there a')))
    print ("")
    print ("Lets get some petscii bytes of a 'HI THERE' ascii string")
    pet_bytes=asc_to_pet_s("HI THERE")
    print "Got back petscii %s"%pet_bytes
    print "Now lets translate the petscii bytes to ascii bytes"
    tr_msg=''
    for b in pet_bytes:
        b_trans = pet_to_asc_b(b)
        tr_msg='%s%s'%(tr_msg,chr(b_trans))
        #print "From petscii %s we got back ascii %s which as a character is %s"%(b,b_trans,chr(b_trans))
    print "From ascii Translated to petscii %s"%tr_msg
    print ("")
    print "Great it works lets try a different ascii string 'hi there' of lower characters"
    pet_bytes=asc_to_pet_s("hi there")
    print "Got back petscii %s"%pet_bytes
    print ("")
    tr_msg=''
    print "Now lets translate the petscii bytes to ascii bytes"
    for b in pet_bytes:
        b_trans = pet_to_asc_b(b)
        tr_msg='%s%s'%(tr_msg,chr(b_trans))
        #print "From petscii %s we got back ascii %s which as a character is %s"%(b,b_trans,chr(b_trans))
    print "From ascii Translated to petscii %s"%tr_msg
    print ("")
    print ("Lets get some ascii bytes of a 'HI THERE' ascii string")
    #asc_bytes=pet_to_asc_s("hi there")
    msg="HI THERE"
    asc_bytes=get_bytes(msg)
    print "Got back ascii %s"%asc_bytes
    print "Now lets translate the ascii bytes to petcii bytes"
    tr_msg=''
    for b in asc_bytes:
        b_trans = asc_to_pet_b(b)
        tr_msg='%s%s'%(tr_msg,chr(b_trans))
        #print "From ascii %s we got back petscii %s which as a character is %s"%(b,b_trans,chr(b_trans))
    print "From ascii Translated to petscii %s"%tr_msg
    print ("")
    print "Great it works lets try a different ascii string 'hi there' of lower characters"
    msg="hi there"
    asc_bytes=[ord(elem) for elem in msg]
    print "Got back ascii %s"%asc_bytes
    print "Now lets translate the ascii bytes to petcii bytes"
    tr_msg=''
    for b in asc_bytes:
        b_trans = asc_to_pet_b(b)
        tr_msg='%s%s'%(tr_msg,chr(b_trans))
        #print "From ascii %s we got back petscii %s which as a character is %s"%(b,b_trans,chr(b_trans))
    print "From ascii Translated to petscii %s"%tr_msg
    print ""
    print "this is the behaviour i would expect ... thanks andi"
    print ""
    print ""
    print "Lets try some byte arrays"
    msg="hi there"
    asc_bytes=[ord(elem) for elem in msg]
    print "Got back ascii %s"%asc_bytes
    print "Now lets translate the ascii bytes to petcii bytes"
    tr_msg=''
    pet_bytes = asc_to_pet_b_arr(asc_bytes)
    
    for b in pet_bytes:
    #    b_trans = asc_to_pet_b(b)
        tr_msg='%s%s'%(tr_msg,chr(b))
        #print "From ascii %s we got back petscii %s which as a character is %s"%(b,b_trans,chr(b_trans))
    print "From ascii Translated to petscii %s"%tr_msg
    print ""
    print ""
    print "Lets try function overloading"
    print("String 'HI THERE A' to ascii(String): " +  str(pet_to_asc_s("HI THERE A",result_type='string')))
    print("String 'HI THERE A' to ascii(String) again: " +  str(pet_to_asc_s('HI THERE A',result_type='string')))
    print("String 'hi there a' to ascii(String): " +  str(pet_to_asc_s("hi there a",result_type='string')))
    print("String 'HI THERE A' to petscii(String): " + str(asc_to_pet_s("HI THERE A",result_type='string')))
    print("String 'hi there a' to petscii(String): " + str(asc_to_pet_s("hi there a",result_type='string')))
    print ""
    print ""
    print "Lets try more function overloading"
    print "get string (as ascii) from string(as pet) using 'ALL CAPS'"
    print pet_to_asc_b_arr(get_bytes("ALL CAPS"),result_type='string')
    print "get string (as ascii) from string(as pet) using 'no caps'"
    print pet_to_asc_b_arr(get_bytes("no caps"),result_type='string')
    print "get string (as petscii) from string(as asc) using 'ALL CAPS'"
    print asc_to_pet_b_arr(get_bytes("ALL CAPS"),result_type='string')
    print "get string (as ascii) from string(as pet) using 'no caps'"
    print asc_to_pet_b_arr(get_bytes("no caps"),result_type='string')
    
    
#examples()

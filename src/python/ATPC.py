"""
Purpose: Convert single character of ASCII to PETSCII and vice versa.
         Also converts string of ASCII to list of hex PETSCII values.
"""

import tables
import logging

logging.basicConfig(filename='conv.log',level=logging.DEBUG)

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


def pet_to_asc_s(in_str):
    """
    Purpose: converts PETSCII string to ASCII
    TODO: clearly this is not implemented yet
    """
    # not sure if you need this or what you'd pass in
    logging.debug("in pet_to_asc_s "+str(in_str))
    ret = []
    for in_char in in_str:
        ret.append(pet_to_asc_c(in_char))
    return ret


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


def asc_to_pet_s(in_str):
    """
    Purpose: converts ASCII string to list of PETSCII hex values
    Input: ASCII string
    Output: returns list of hex values of PETSCII characters
    """
    logging.debug("in asc_to_pet_s")
    ret = []
    for in_char in in_str:
        ret.append(asc_to_pet_c(in_char))
    return ret


def examples():
    """
    Purpose: runs through some simple examples
    Input: nothing
    Output: Side effect is that things are printed to the screen
    """
    logging.info("Lets Run some Test cases")
    print("\n\nKEEP IN MIND THAT THE RETURN VALUE IS JUST AN INTEGER")
    print("c in ascii to petscii: " + str(asc_to_pet_c('c')))
    print("A in ascii to petscii: " + str(asc_to_pet_c('A')))
    print("")
    print("String 'hi there A' to petscii: " + str(asc_to_pet_s("HI THERE A")))
    print ("")
    print("petscii 'c' to ascii: " + str(pet_to_asc_c('c')))
    print("petscii 'A' to ascii: " + str(pet_to_asc_c('A')))
    print("String 'hi there A' to ascii: " +  str(pet_to_asc_s('HI THERE A')))
    print ("")
    

examples()

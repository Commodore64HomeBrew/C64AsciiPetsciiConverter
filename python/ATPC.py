import tables
import logging

def pet_to_asc_c(in_char):
    in_char = chr(in_char)
    logging.info("in petToPetC")
    if len(in_char) != 1:
        logging.warning("in petToPetC")
        logging.warning("you are calling the wrong function")
        logging.warning("parameter should be a single character")
        return -1
    ret = tables.petToAscTable[ord(in_char)]
    logging.info("pet character: " + str(ord(in_char)) + " to " + str(chr(ret)))
    print("the pet character: " + str(ord(in_char)) + " to " + str(chr(ret)))

def pet_to_asc_s(in_str):
    # not sure if you need this or what you'd pass in
    logging.info("in pet_to_asc_s "+str(in_str))


def asc_to_pet_c(in_char):
    logging.info("in asc_to_pet_c")
    if len(in_char) != 1:
        logging.warning("in asc_to_pet_c")
        logging.warning("you are calling the wrong function")
        logging.warning("parameter should be a single character")
        return -1
    ret = tables.ascToPetTable[ord(in_char)]
    logging.info("ascii character: " + str(in_char) + " to " + str(ret))
    print("ascii character: " + str(in_char) + " to " + str(ret))
    return ret

def asc_to_pet_s(in_str):
    logging.info("in asc_to_pet_s")
    ret = []
    for in_char in in_str:
        ret.append(asc_to_pet_c(in_char))
    print ret
    return ret


def examples():
    asc_to_pet_c('c')
    asc_to_pet_c('A')
    print("")
    asc_to_pet_s("hi there A")
    print ("")
    pet_to_asc_c(67)
    pet_to_asc_c(193)
    pet_to_asc_s('hi there')

examples()

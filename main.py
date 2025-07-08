from playsound3 import playsound

import voices

def gen_one_digit(numstr, vl): # pretty simple - add plain number if not 0
    if int(numstr[2]) != 0:
        vl.append(voices.plain_numbers()[int(numstr[2])])
    return vl

def gen_ten_digit(numstr, vl): # digit 2 - gets complicated with teens here
    if numstr[1] == '0':
        return gen_one_digit(numstr, vl)

    #TEEN LOGIC
    if int(numstr[1]) == 1:
        #10
        if int(numstr[2]) == 0:
            vl.append(voices.plain_numbers()[10])
            return vl
        #11
        if int(numstr[2]) ==  1:
            vl.append(voices.plain_numbers()[11])
            return vl
        #12
        if int(numstr[2]) == 2:
            vl.append(voices.plain_numbers()[12])
            return vl
        #13
        if int(numstr[2]) == 3:
            vl.append(voices.thir())
            vl.append(voices.teen())
            return vl
        #14
        if int(numstr[2]) == 5:
            vl.append(voices.fif())
            vl.append(voices.teen())
            return vl
        #ALL OTHER TEENS
        vl.append(voices.plain_numbers()[int(numstr[2])])
        vl.append(voices.teen())
        return vl
    
    #TWENTIES
    if int(numstr[1]) == 2:
        vl.append(voices.twen())
        vl.append(voices.ty())
        return gen_one_digit(numstr, vl)
    
    #THIRTIES
    if int(numstr[1]) == 3:
        vl.append(voices.thir())
        vl.append(voices.ty())
        return gen_one_digit(numstr, vl)
    
    #FIFTIES
    if int(numstr[1]) == 5:
        vl.append(voices.fif())
        vl.append(voices.ty())
        return gen_one_digit(numstr, vl)
    
    vl.append(voices.plain_numbers()[int(numstr[1])])
    vl.append(voices.ty())
    return gen_one_digit(numstr, vl)

def gen_hundred_digit(numstr, vl): # digit 3
    if numstr[0] == '0':
        return gen_ten_digit(numstr, vl)
    
    vl.append(voices.plain_numbers()[int(numstr[0])]) # simply add the voice of the digit in the hundreds column
    vl.append(voices.hundred())
    return gen_ten_digit(numstr, vl)

def get_voice_list(numstr): # will return a list of voices to play to sound like the input number
    vl = []
    if len(numstr) <= 3:
        voice_list = gen_hundred_digit(numstr, vl)
    else:
        voice_list = None

    return voice_list

def conv_str_int_to_three_letters(str_int):
    new_str = ""
    
    if len(str_int) == 3:
        return str_int
    elif len(str_int) == 2:
        new_str = '0'
        new_str += str_int
        return new_str
    elif len(str_int) == 1:
        new_str = '00'
        new_str += str_int
        return new_str
        
            

def bopit_say(numberstr):
    voice_list = get_voice_list(numberstr)

    if voice_list == None:
        voice_list = []
        voice_list.append(voices.random_error())

    for i in range(len(voice_list)):
        playsound(voice_list[i])

while True:
    bopit_say(conv_str_int_to_three_letters(input("BopIt Says: ")))
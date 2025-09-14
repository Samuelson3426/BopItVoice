try:
    from playsound3 import playsound
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("Please install playsound3 using pip: 'pip install playsound3'")

try:
    import voices
except:
    raise FileNotFoundError("main.py needs to be in the same directory as voices.py to function correctly.")

from sys import argv
import time

greet_text = 'Enter number for Bop It to say (1-999): '

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

def count_to_999():
    try:
        for i in range(1000):
            if i > 0:
                init_time = time.time()
                bopit_say(conv_str_int_to_three_letters(str(i)))
                while (time.time() - init_time) < 1:
                    pass
    except KeyboardInterrupt:
        return
    
def countdown_from_10():
    i = 10
    try:
        while i > 0:
            init_time = time.time()
            bopit_say(conv_str_int_to_three_letters(str(i)))
            i-=1
            while (time.time() - init_time) < 1:
                pass
    except KeyboardInterrupt:
        return

def conv_str_int_to_three_letters(str_int):
    if str_int == "":
        count_to_999()
        return "count" # invalid value
    
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
    if numberstr == "count": # invalid value from counting finish
        print()
        return
    elif numberstr == None:
        numberstr = "No"

    try:
        if int(numberstr) < 1 or int(numberstr) > 999:
            voice_list = [voices.random_error()]
        else:
            voice_list = get_voice_list(numberstr)
    except (TypeError, ValueError):
        voice_list = [voices.random_error()]

    print()
    for i in range(len(voice_list)):
        print(voice_list[i])
        playsound(voice_list[i])
    print(f'{dash_string_for(numberstr)}\n{numberstr}')


def dash_string_for(string):
    newstr = ""
    for i in range(len(string)):
        newstr += '='
    return newstr

def main():
    playsound(voices.bop_it())
    while True:
        try:
            print(dash_string_for(greet_text))
            usr_input = input(greet_text)
        except KeyboardInterrupt as e:
            print("\nBye :)")
            playsound(voices.random_error())
            break

        bopit_say(conv_str_int_to_three_letters(usr_input))

if len(argv) > 1:
    if argv[1] == "count" or argv[1] == "Count" or argv[1] == "-count":
        count_to_999()
    elif argv[1] == "countdown" or "Countdown" or "-countdown":
        countdown_from_10()
elif __name__ == "__main__":
    main()
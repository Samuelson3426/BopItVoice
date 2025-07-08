from playsound3 import playsound

import voices

def check_number(numstr): # will return a list of voices to play to sound like the input number
    voice_list = []
    
    if int(numstr) > 0 and int(numstr) <= 12:
        voice_list.append(voices.plain_numbers()[int(numstr)])
        return voice_list
    
    if len(numstr) == 2 and int(numstr) > 12: # 2 digit numbers (>plain (which is >12))
        
        # TEEN NUMBERS
        if int(numstr[0]) == 1:
            
            if int(numstr[1]) == 3: #13
                voice_list.append(voices.thir())
                voice_list.append(voices.teen())
                return voice_list
            
            if int(numstr[1]) == 5: #15
                voice_list.append(voices.fif())
                voice_list.append(voices.teen())
                return voice_list
            
            voice_list.append(voices.plain_numbers()[int(numstr[1])])
            voice_list.append(voices.teen())
            return voice_list
            
            

def bopit_say(numberstr):
    voice_list = check_number(numberstr)

    if voice_list == None:
        voice_list = []
        voice_list.append(voices.twen())

    for i in range(len(voice_list)):
        playsound(voice_list[i])

while True:
    bopit_say(input("BopIt Says: "))
import os
from random import randint

VOICE_PATH = 'BopItExtreme2-Numbers'
VOICE_PATH_ERROR = 'BopItExtreme2-Error'
VOICE_BOP_IT = 'BobItExtreme2-BopIt.wav'

def bop_it():
    return VOICE_BOP_IT

def plain_numbers():
    sdv = []
    for i in range(13): # all low numbers with a single voiceline
        if i != 0:
            sdv.append(os.path.join(VOICE_PATH, f'{i}.wav'))
        else:
            sdv.append("0.wav")
    return sdv

def random_error():
    x = []
    all_files = os.listdir(VOICE_PATH_ERROR)
    for i in range(len(all_files)):
        if all_files[i].endswith('.wav'):
            x.append(os.path.join(VOICE_PATH_ERROR, all_files[i]))
    return x[randint(0, len(x)-1)]

def fif():
    return os.path.join(VOICE_PATH, 'Fif-.wav')

def hundred():
    return os.path.join(VOICE_PATH, 'Hundred.wav')

def thir():
    return os.path.join(VOICE_PATH, 'Thir-.wav')

def twen():
    return os.path.join(VOICE_PATH, 'Twen-.wav')

def teen():
    return os.path.join(VOICE_PATH, '-teen.wav')

def ty():
    return os.path.join(VOICE_PATH, '-ty.wav')
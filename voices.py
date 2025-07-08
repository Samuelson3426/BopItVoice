import os
from random import randint

voice_path = 'BopItExtreme2-Numbers'
voice_path_error = 'BopItExtreme2-Error'
voice_bop_it = 'BobItExtreme2-BopIt.wav'

def bop_it():
    return voice_bop_it

def plain_numbers():
    sdv = []
    for i in range(13): #first 12 numbers
        if i != 0:
            sdv.append(os.path.join(voice_path, f'{i}.wav'))
        else:
            sdv.append("0.wav")
    return sdv

def random_error():
    x = []
    all_files = os.listdir(voice_path_error)
    for i in range(len(all_files)):
        if all_files[i].endswith('.wav'):
            x.append(os.path.join(voice_path_error, all_files[i]))
    return x[randint(0, len(x)-1)]

def fif():
    return os.path.join(voice_path, 'Fif-.wav')

def hundred():
    return os.path.join(voice_path, 'Hundred.wav')

def thir():
    return os.path.join(voice_path, 'Thir-.wav')

def twen():
    return os.path.join(voice_path, 'Twen-.wav')

def teen():
    return os.path.join(voice_path, '-teen.wav')

def ty():
    return os.path.join(voice_path, '-ty.wav')
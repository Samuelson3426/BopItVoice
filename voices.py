import os

voice_path = 'BopItExtreme2-Numbers'

def plain_numbers():
    sdv = []
    for i in range(13): #first 12 numbers
        if i != 0:
            sdv.append(os.path.join(voice_path, f'{i}.wav'))
        else:
            sdv.append("0.wav")
    return sdv

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
# Kramer Kilroy
# CSCI 102-Section A
# Week 12 - Part



def PrintOutput(a):
    print('OUTPUT',a)



def LoadFile (file_name):
    file = open(file_name, 'r')
    text = file.read()
    text = text.split('\n')
    return text


def UpdateString(string_1, string_2, n):
    n = int(n)
    string_1 = string_1[:n] + string_2 + string_1[n + 1:] 
    print('OUTPUT', string_1)

def FindWordCount (list_1, string_3):
    string_a = ''.join(list_1)
    string_b = string_a.split(' ')
    count = 0
    for char in string_b:
        if char == string_3:
            count = count + 1
    return count

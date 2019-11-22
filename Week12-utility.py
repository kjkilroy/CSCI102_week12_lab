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

def ScoreFinder (list_a, list_b, string_a):
    string_a = string_a.lower()
    list_a1 = []
    for char in list_a:
        char = char.lower()
        list_a1.append(char)
    string_c = ' '.join(list_a1)
    b = string_c.find(string_a)
    for char in list_a1:
        if char == string_a:
            a = list_a1.index(char)
            print('OUTPUT',list_a[a],'got a score of ',list_b[a])
    if b == -1:
        print('OUTPUT player not found')


def Union (list_c,list_d):
    new_list = list_c + list_d
    return new_list




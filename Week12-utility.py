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

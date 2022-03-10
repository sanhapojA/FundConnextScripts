# function read text files.
from os import path


def read_text(startLine, filesName):
    readTxt = []
    with open(filesName, 'r', encoding='UTF-8') as fn:
        readFilesName = fn.readlines()
        for i in range(startLine, len(readFilesName)):
            readCol = readFilesName[i].split('|')
            readTxt.append(readCol)
    return readTxt

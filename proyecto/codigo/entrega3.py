import numpy as np
from numpy import genfromtxt

def nearestCompression(path):
    image = genfromtxt(path, delimiter=',')

    imagenNueva = []

    for i in range(0, len(image)-1, 2):
        nuevaFila = []
        for j in range(0, len(image[0])-1, 2):
            nuevaFila.append(image[i][j])
        imagenNueva.append(nuevaFila)

    imagenNuevaNP = np.array(imagenNueva)
    return imagenNuevaNP

def transformToList(image):
    nRows, nColumns = image.shape
    list = []
    for i in range(nRows):
        for j in range(nColumns):
            list.append(image[i][j])
    return list

def comprimirLZ77(list):
    i = 0
    listN = []
    while i < len(list):
        match = findMatch(list, i)
        if match:
            matchDistance, matchLength = match
            diferentAdded = min(i+matchLength, len(list)-1)
            listN.append("<" + str(matchDistance) + "," + str(matchLength) + "," + str(list[diferentAdded]) + ">")
            i = i + matchLength+1
        else:
            listN.append('<0,0,' + str(list[i]) + '>')
            i = i + 1
    return listN

def findMatch(list, i):
    historyWindowSize = 20
    lookAheadWindowSize = 20
    endOfTheBuffer = min(i + lookAheadWindowSize, len(list) + 1)

    matchDistance = -1
    matchLength = -1

    for j in range(i, endOfTheBuffer):
        startIndex = max(0, i - historyWindowSize)
        subList = list[i:j+1]
        for m in range(startIndex, i):
            repetitions = len(subList)//(i-m)
            last = len(subList)%(i-m)

            matchedList = list[m:i] * repetitions + list[m:m+last]

            if matchedList == subList and len(subList)>matchLength:
                matchDistance = i - m
                matchLength = len(subList)
    if matchDistance > 0 and matchLength > 0:
        return (matchDistance, matchLength)
    return None

def descomprimir(compressedList):
    decompressList = []
    i = 0
    while i < len(compressedList):
        decompressing = compressedList[i]
        firstComma = decompressing.index(',')
        secondComma = decompressing.index(',', firstComma + 1)
        if compressedList[i][1:firstComma] == '0':
            decompressList.append(compressedList[i][secondComma+1:decompressing.index('>')])
            i = i + 1
        else:
            if compressedList[i][firstComma+1:secondComma] == '1':
                number = decompressList[-(int(compressedList[i][1:firstComma]))]
                decompressList.append(number)
                decompressList.append(compressedList[i][secondComma+1:decompressing.index('>')])
                i = i + 1
            else:
                temporalList = []
                f = -(int(compressedList[i][1:firstComma]))
                m = int(compressedList[i][firstComma+1:secondComma])
                if abs(f) > m:
                    while m > 0:
                        temporalList.append(decompressList[f])
                        f = f + 1
                        m = m - 1
                    for item in temporalList:
                        decompressList.append(item)
                    decompressList.append(compressedList[i][secondComma+1:decompressing.index('>')])
                    i = i + 1
                else:
                    save = m - int(compressedList[i][1:firstComma])
                    m = int(compressedList[i][1:firstComma])
                    while m > 0:
                        temporalList.append(decompressList[f])
                        f = f + 1
                        m = m - 1
                    for item in temporalList:
                        decompressList.append(item)
                    while save > 0:
                        decompressList.append(decompressList[-1])
                        save = save - 1
                    decompressList.append(compressedList[i][secondComma+1:decompressing.index('>')])
                    i = i + 1
    return decompressList

def main():
    firstCompression = nearestCompression('2.csv')
    list = transformToList(firstCompression)
    secondCompression = comprimirLZ77(list)
    f = open('imagen_comprimida', 'w')
    for i in range(len(secondCompression)-1):
        f.write(secondCompression[i])
        f.write(',')
    f.write(secondCompression[-1])
    f.close()
    print('-'*44, 'La imagen fue comprimida exitosamente', '-'*44)
main()
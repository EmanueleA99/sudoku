#!/usr/bin/env python3

import sys
import csv

# Check if number of arguments is exactly 2
if len(sys.argv) != 2:
    print("Utilizzo:", sys.argv[0], "<griglia input>")
    quit()

# load the problem
reader = csv.reader(open(sys.argv[1], "r"), delimiter=",")
mat = list(reader)

# TODO: solve the problem!
def CreaMatrix(mat):  # crea la matrice di possibilità
    for i in range(0, 16):
        for j in range(0, 16):
            if (mat[i][j] == ""):  # se nella casella non c'è il numero
                valori = Possibility(i, j, mat)  # ritorna stringa di possibilità
                mat[i][j] = valori  # aggiungo le possibilità
    return mat


def Possibility(i, j, mat):  # restituisce le possibilità data una casella
    # lavorare su sudoku originale "mat"
    list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]  # vettore possibilità
    for k in range(0, 16):  # controllo riga
        if mat[i][k] != "":
            if mat[i][k] in list:
                list.remove(mat[i][k])
    for k in range(0, 16):  # controllo colonna
        if mat[k][j] != "":
            if mat[k][j] in list:
                list.remove(mat[k][j])
    blocco = blockToList(mat, i, j)
    for k in range(0, 16):
        if blocco[k] != "":
            if blocco[k] in list:
                list.remove(blocco[k])
    return list


def searchBlock(i):  # cerca indici del blocco
    if ((i % 4) != 0):
        if i < 4:
            i = 0
        elif (i < 8 and i > 4):
            i = 4
        elif (i < 12 and i > 8):
            i = 8
        else:
            i = 12
    return i


def blockToList(mat, i, j):  # trasforma blocco in lista per il controllo
    indexi = searchBlock(i)
    indexj = searchBlock(j)
    b = []
    for h in range(indexi, indexi + 4):
        for k in range(indexj, indexj + 4):
            b = b + [mat[h][k]]
    return b


def blockToList2(mat, i, j):  # trasforma blocco in lista per il controllo
    indexi = searchBlock(i)
    indexj = searchBlock(j)
    b = []
    for h in range(indexi, indexi + 4):
        for k in range(indexj, indexj + 4):
            if (h != i) or (k != j):  # non metto l'elemento che ha chiamato la funzione
                if type(mat[h][k]) is list:
                    for w in range(0, len(mat[h][k])):
                        b.append(mat[h][k][w])
    return b


def trovaSingoli(valoriMancanti):  # vede dove c'è una sola possibilità e la inserisce nella soluzione
    global mat
    for i in range(0, 16):
        for j in range(0, 16):
            if type(mat[i][j]) is list:  # vedo se è una lista di numeri, quindi non è ancora assegnato
                if len(mat[i][j]) == 1:  # se il numero è uno solo
                    a = mat[i][j][0]  # salvo valore
                    mat[i][j] = a  # sostiutuisco
                    valoriMancanti = valoriMancanti - 1
                    rimuoviProb(i, j, a)  # rimuovo "a" nelle probabilità delle righe, colonne e blocchi
                    return valoriMancanti
    return valoriMancanti


def rimuoviProb(i, j, valore):
    global mat
    for k in range(0, 16):  # rimuovo dalle righe
        if type(mat[i][k]) is list:  # vedo se è una lista
            if valore in mat[i][k]:  # vedo se il numero da togliere c'è
                mat[i][k].remove(valore)  # lo rimuovo
    for k in range(0, 16):  # rimuovo dalle colonne
        if type(mat[k][j]) is list:  # stesse operazioni precedenti
            if valore in mat[k][j]:
                mat[k][j].remove(valore)
    block = blockToList(mat, i, j)  # faccio una lista del blocco
    for k in range(0, 16):
        if type(block[k]) is list:
            if valore in block[k]:
                block[k].remove(valore)


def trovaBlocchi(valoriMancanti):
    global mat
    for i in range(0, 16):
        for j in range(0, 16):
            if type(mat[i][j]) is list:
                for k in range(0, len(mat[i][j])):
                    newlist = blockToList2(mat, i, j)
                    if mat[i][j][k] not in newlist:
                        a = mat[i][j][k]  # salvo valore
                        mat[i][j] = a  # sostiutuisco
                        valoriMancanti = valoriMancanti - 1
                        rimuoviProb(i, j, a)
                        for i in range(0, 16):  # stampo soluzione
                            print(mat[i])
                        return valoriMancanti
    return valoriMancanti


def RisolviSudoku(mat):  # inserire come input un sudoku esadecimale
    matrix = CreaMatrix(mat)
    valoriMancanti = 0
    for i in range(0, 16):
        for j in range(0, 16):
            if type(matrix[i][j]) is list:
                valoriMancanti = valoriMancanti + 1
    while (valoriMancanti != 0):
        ispezione = valoriMancanti
        valoriMancanti = trovaSingoli(valoriMancanti)
        if ispezione == valoriMancanti:  # se il primo algoritmo non è sufficiente utilizzo il secondo
            valoriMancanti = trovaBlocchi(valoriMancanti)
    return matrix  # ritorno soluzione


soluzione = RisolviSudoku(mat)

# dump the output
wtr = csv.writer(open ('soluzione.csv', 'w'), delimiter=',', lineterminator='\n')
for x in soluzione : wtr.writerows([x])

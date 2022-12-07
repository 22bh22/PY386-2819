# Create a spiral matrix from a given list
def printSpiralOrder(N):
    # base case
    #A = [[if len(i)<len(N**2) "0" * (len(N**2)-len(i)) + str(i) else i] for i in range(1, N**2 + 1)]
	A = [i for i in range(1, N**2 + 1)]
    #print(A)
    top = left = 0
    bottom = N - 1
    right = N - 1
 
    # construct an `M × N` matrix
    mat = [[0 for x in range(N)] for y in range(N)]
 
    index = 0
 
    while True:
 
        if left > right:
            break
 
        # print top row
        for i in range(left, right + 1):
            mat[top][i] = A[index]
            index = index + 1
        top = top + 1
 
        if top > bottom:
            break
 
        # print right column
        for i in range(top, bottom + 1):
            mat[i][right] = A[index]
            index = index + 1
        right = right - 1
 
        if left > right:
            break
 
        # print bottom row
        for i in range(right, left - 1, -1):
            mat[bottom][i] = A[index]
            index = index + 1
        bottom = bottom - 1
 
        if top > bottom:
            break
 
        # print left column
        for i in range(bottom, top - 1, -1):
            mat[i][left] = A[index]
            index = index + 1
        left = left + 1
        XXX = []
    for r in mat:
        print(r)
        XXX.append(r)
    return XXX
 
 

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "spiral_output.txt"
abs_file_path = os.path.join(script_dir, rel_path)

N = int(input("Введите размер спирали: "))
n = int(input("Введите число спиралей: "))
if N > 0 and n > 0:
        XXX = printSpiralOrder(N)
        #print(XXX)
        with open(abs_file_path, 'a', encoding="UTF-8") as file:
            for i in XXX:
                file.write((str(i) + chr(32)) * n + chr(10))

else:
    print("Ошибка! Введённое число ", n, " отрицательное. Выполнение программы остановлено.", sep="")
input("Для завершения нажмите любую клавишу...")
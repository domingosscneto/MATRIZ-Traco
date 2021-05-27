#Calcula o traço (soma dos elementos da diagonal principal) de uma matriz quadrada
N = int(input('Digite o número de linha e colunas de sua matriz quadrada: '))
A = [[0 for x in range(N)] for y in range(N)]
T = [0]
print(A)

def preencheMatriz():
    print('Digite os elementos de sua matriz:')
    for i in range(N):
        for j in range(N):
            A[i][j] = int(input())
    print('Matriz A:')
    print(A)
    print('')
    for i in range(N):
        for j in range(N):
            print(A[i][j], '', end='')
        print()
    print('')

def calculaTraço():
    for i in range(N):
        for j in range(N):
            if A[i][i] in T:
                break
            else:
                T.append(A[i][i])

def somatoria():
    soma = sum(T)
    print(f'Traço da matriz A: {soma}')



preencheMatriz()
calculaTraço()
somatoria()
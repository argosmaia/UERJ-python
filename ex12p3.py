'''Elabore um programa que leia uma matriz de tamanho mxm elementos inteiros
e, determine o menor valor da matriz. Imprimir a matriz lida e o resultado obtido
com mensagens indicativas.'''

def Gera():
    try:
        m = int(input('Digite um termo para o quadrado: '))
    except ValueError:
        print('Erro. Tente novamente...')
        m = int(input('Digite um termo para o quadrado: '))
    return m

def Forma(m):
    a = [None] * m
    for i in range(m):
        a[i] = [None] * m
        for j in range(m):
            while True:
                try:
                    a[i][j] = float(input('Digite A = ['+str(i+1)+'],['+str(j+1)+']: '))
                    break
                except ValueError:
                    print('Erro na matriz. Digite novamente...')
    return a

def Minimo(a):
    linha = 0
    linha = int(input('Digite a linha a ser percorrida: '))
    menor = a[0][0]
    for r in range(len(a)):
        if linha == a[r]:
            nums = a[r]
            for n in nums:
                menor = n if menor > n else menor
    return linha, menor

def Impr(a, menor):
    #Printa a funcao
    print('O menor valor da linha {:.2f} eh {:.2f}'.format(linha, menor))
    print ('\nMatriz Lida\n')
    for i in range(m):
        for j in range(m):
            print ('|{:.2f}|'.format(a[i][j]),end=' ')
        print()
    return

m = Gera()
a = Forma(m)
menor = Minimo(a)
Impr(a, menor)
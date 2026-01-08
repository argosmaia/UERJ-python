'''Elabore um programa que leia uma matriz quadrada de tamanho mxm e
determine o somatório de todos os números presentes na diagonal secundária
da matriz. Imprimir a matriz lida sob a forma de tabela e o resultado obtido.'''

def ler_inteiro(mensagem, mensagem_erro="Erro. Digite um número inteiro válido: "):
    """Lê e valida entrada de inteiros, evitando repetição de código."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print(mensagem_erro)

def ler_matriz(m):
    """Lê uma matriz mxm de valores float com validação."""
    matriz = []
    for i in range(m):
        linha = []
        for j in range(m):
            valor = ler_inteiro(
                f'Digite A[{i+1}][{j+1}]: ',
                'Erro na matriz. Digite um número válido: '
            )
            linha.append(float(valor))
        matriz.append(linha)
    return matriz

def soma_diagonal_secundaria(matriz):
    """Calcula a soma da diagonal secundária de forma eficiente."""
    return sum(matriz[i][len(matriz)-1-i] for i in range(len(matriz)))

def imprimir_resultado(matriz, soma):
    """Imprime a matriz formatada e o resultado da soma."""
    print("\nMatriz lida:")
    for linha in matriz:
        print(" ".join(f"|{valor:7.2f}|" for valor in linha))
    
    print(f"\nSoma da diagonal secundária: {soma:.2f}")

def main():
    """Função principal que orquestra a execução do programa."""
    # Entrada da dimensão
    m = ler_inteiro('Digite a dimensão da matriz quadrada (m): ')
    
    # Validação básica
    if m <= 0:
        print("Dimensão inválida. O programa será encerrado.")
        return
    
    # Leitura da matriz
    matriz = ler_matriz(m)
    
    # Cálculo da soma
    soma = soma_diagonal_secundaria(matriz)
    
    # Exibição dos resultados
    imprimir_resultado(matriz, soma)

# Execução do programa
if __name__ == "__main__":
    main()

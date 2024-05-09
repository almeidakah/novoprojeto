''' Escreva um programa que leia 10 valores inteiros e positivos e  
a) encontre o maior valor;
b) encontre o menor valor;
c)   calcule a média dos números lidos."'''

def main():
  """
  Este programa lê 10 valores inteiros e positivos, encontra o maior e o menor valor, e calcula a média dos números lidos.
  """
  # Inicializa variáveis para armazenar o maior e menor valor
  maior_valor = None
  menor_valor = None

  # Inicializa variável para somar os valores lidos
  soma = 0

  # Lê 10 valores
  for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor: "))

    # Valida se o valor é positivo
    if valor <= 0:
      print("Erro: O valor digitado deve ser positivo.")
      continue

    # Atualiza o maior valor
    if maior_valor is None or valor > maior_valor:
      maior_valor = valor

    # Atualiza o menor valor
    if menor_valor is None or valor < menor_valor:
      menor_valor = valor

    # Soma o valor lido
    soma += valor

  # Calcula a média
  media = soma / 10

  # Imprime os resultados
  print(f"Maior valor: {maior_valor}")
  print(f"Menor valor: {menor_valor}")
  print(f"Média: {media:.2f}")  # Formata a média com duas casas decimais

if __name__ == "__main__":
  main()

'''
    Peça para o usuario digitar o nome do aluno e digitar 2 notas do aluno e calcular a media
'''
aluno = str(input("Digite o nome do aluno: "))
nota1 = float(input("digite a primeira nota "))
nota2 = float(input("digite a segunda nota "))
media = (nota1 + nota2) /2
print ("O aluno ", aluno, "tirou a nota " ,media )

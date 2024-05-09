'''  Escreva um programa que leia uma temperatura, pergunte a unidade dessa temperatura e converta o valor para as demais unidades (As unidades de temperatura são Celsius, Kelvin e Fahrenheit).'''

temperatura = float(input("informe a temperatura ? "))
unidade = str(input("infome a unidade da temperatura ? " ))


ctemf = temperatura * 1.8 + 32  
ctemk = temperatura + 273.15 
ftemc = (temperatura-32)/1.8
ftemk = ((temperatura- 32)/1.8)+273.15
ktemf = ((temperatura-273.15)*1.8)+32
ktemc = temperatura - 273.15 

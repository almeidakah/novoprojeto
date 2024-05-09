'''
    Faça um programa que pergunte o valor em graus para o usuario e converta 1 para fahrenheit e outro para 2 para kelvin
'''

temperatura1 = float(input("informe a temperatura: "))
temf = temperatura1 * 1.8 + 32  
temk = temperatura1 + 273.15 
 
print(" ela em celsius é {}, em farenheit é {}, e em kelvin é {}" .format(temperatura1,temf,temk))
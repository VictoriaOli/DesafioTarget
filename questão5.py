# Questão 5

"""
    Escreva um programa que inverta os caracteres de um string.
"""

def inverter_string(string): 
    invertida = ""
    
    for char in string:
        invertida = char + invertida
    return invertida

recebida = inverter_string("cadeira")

print(recebida)

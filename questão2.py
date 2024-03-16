# Questão 2
""" 
	2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será 
	a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
	escreva um programa na linguagem que desejar onde, informado um número, 
	ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

## num é o número que se deseja verificar se está na sequência de Fibonacci
def fibonacci(num):
	fibonacci_sequence = [0, 1]  # Os 2 primeiros termos
	aux = True # Variavel auxiliar para identificar quando o número pode não estar dentro da sequência
	
	while aux:
		next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # O próximo termo é a soma dos dois últimos
		fibonacci_sequence.append(next_term)
		if next_term > num:
			aux = False
		if next_term == num:
			break
	return aux


# Exemplo de uso
num = 4 
resultado = fibonacci(num)

if resultado:
	print(f"O número {num} está em Fibonacci")
else:
	print(f"O número {num} não está em Fibonacci") 
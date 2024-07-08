texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# exemplo utilizando um interavel 
for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")
	
else:
    print()  # adiciona uma quebra de linha


# exemplo utilizando a função built-in range	
for numero in range(0,51, 5):
	print(numero,end=" ")
	

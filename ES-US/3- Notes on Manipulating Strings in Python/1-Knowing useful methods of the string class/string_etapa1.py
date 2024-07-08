nome = "GuSTaVO"

#maiusculas,minusculas e titulo
print(nome.upper())
print(nome.lower())
print(nome.title())

#eliminando os espaços em branco
texto = "  Olá mundo!    "
print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".") #só os da esquerda
print(texto.rstrip() + ".") # so os da direita

#Juncoes e centralização
menu = "python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))

print("-".join(menu))

#se fosse com for seria +- assim
for letra in menu:
    print(letra, end="-")
print()



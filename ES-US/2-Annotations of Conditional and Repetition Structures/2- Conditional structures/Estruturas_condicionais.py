MAIOR_IDADE = 18
IDADE_EPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_EPECIAL:
    print("Pode fazer aulas teoricas, mas nao pode fazer as praticas.")
else:
    print("Ainda não pode tirar a CNH")
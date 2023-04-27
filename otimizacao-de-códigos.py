unidades = ['bit','byte','KB','MB','GB','TB','PB']
unidadeInicial = input(f"Insira a unidade inicial: ")

while unidadeInicial not in unidades:
    unidadeInicial = input(f"Insira a unidade inicial: ")

unidadeFinal = input(f"Insira a unidade final: ")

while unidadeFinal not in unidades:
    unidadeFinal = input(f"Insira a unidade final: ")

valor = int(input(f"Insira o valor a ser convertido: "))
posiçãoinicial = 0
posiçãofinal = 0
unidadebit = 'bit'

if unidadeInicial == unidadebit:
    valor3 = valor / 8
    unidadeInicial = "byte"
else:
    valor3 = valor

for i in unidades:
    if i == unidadeInicial:
            posiçãoinicial = unidades.index(i)
    if i == unidadeFinal:
            posiçãofinal = unidades.index(i)
variável = posiçãofinal - posiçãoinicial
valor2= 1024**variável
valor3= valor/valor2

if unidadeFinal == unidadebit:
    valor3 = (valor / 1024)*8

print(f"{valor3:.14f}")
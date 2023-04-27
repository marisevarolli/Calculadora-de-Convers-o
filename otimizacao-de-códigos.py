unidades = ['bit','byte','KB','MB','GB','TB','PB']
unidadeInicial = input(f"Insira a unidade inicial: ")
unidadeFinal = input(f"Insira a unidade final: ")
valor = int(input(f"Insira o valor a ser convertido: "))
posiçãoinicial = 0
posiçãofinal = 0
unidadebit = 'bit'

for i in unidades:
    if i == unidadeInicial:
            posiçãoinicial = unidades.index(i)
    if i == unidadeFinal:
            posiçãofinal = unidades.index(i)
variável = posiçãofinal - posiçãoinicial
valor2= 1024**variável
valor3= valor/valor2

print(f"{valor3:.14f}")
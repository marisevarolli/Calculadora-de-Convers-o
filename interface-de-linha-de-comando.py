from calculadora import converterStringParaFloat, bitParaByte, byteParaBit, byteParaKB, KBParaByte, KBParaMB, MBParaKB, MBParaGB, GBParaMB, GBParaTB, TBParaGB, TBParaPB, PBParaTB

print(' -Escreva 1 para bitParaByte \n -Escreva 2 para byteParaBit \n -Escreva 3 para byteParaKB \n -Escreva 4 para KBParaByte \n -Escreva 5 para KBParaMB \n -Escreva 6 para MBParaKB \n -Escreva 7 para MBParaGB \n -Escreva 8 para GBParaMB \n -Escreva 9 para GBParaTB \n -Escreva 10 para TBParaGB \n -Escreva 11 para TBParaPB \n -Escreva 12 para PBParaTB')
funcEscolha = input()
if(funcEscolha == '1'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '3'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaKB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '4'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KBParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '5'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KBParaMB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '6'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MBParaKB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '7'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MBParaGB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '8'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GBParaMB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '9'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GBParaTB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '10'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TBParaGB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '11'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TBParaPB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '12'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = PBParaTB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)


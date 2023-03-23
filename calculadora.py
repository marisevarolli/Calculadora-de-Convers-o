valorpadrão=1024
def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteParaKB(valorASerConvertido):
    print('Valor convertido de byte para KB')
    KBCalculado = valorASerConvertido / valorpadrão
    return KBCalculado

def KBParaByte(valorASerConvertido):
    print('Valor convertido de KB para byte')
    ByteCalculado = valorASerConvertido * valorpadrão
    return ByteCalculado

def KBParaMB(valorASerConvertido):
    print('Valor convertido de KB para MB')
    MBCalculado = valorASerConvertido / valorpadrão
    return MBCalculado

def MBParaKB(valorASerConvertido):
    print('Valor convertido de MB para KB')
    KBCalculado = valorASerConvertido * valorpadrão
    return KBCalculado

def MBParaGB(valorASerConvertido):
    print('Valor convertido de MB para GB')
    GBCalculado = valorASerConvertido / valorpadrão
    return GBCalculado

def GBParaMB(valorASerConvertido):
    print('Valor convertido de GB para MB')
    MBCalculado = valorASerConvertido * valorpadrão
    return MBCalculado

def GBParaTB(valorASerConvertido):
    print('Valor convertido de GB para TB')
    TBCalculado = valorASerConvertido / valorpadrão
    return TBCalculado

def TBParaGB(valorASerConvertido):
    print('Valor convertido de TB para GB')
    GBCalculado = valorASerConvertido * valorpadrão
    return GBCalculado

def TBParaPB(valorASerConvertido):
    print('Valor convertido de TB para PB')
    PBCalculado = valorASerConvertido / valorpadrão
    return PBCalculado

def PBParaTB(valorASerConvertido):
    print('Valor convertido de PB para TB')
    TBCalculado = valorASerConvertido * valorpadrão
    return TBCalculado



def codificador():
    
    frase = input('Digite a frase a ser encriptada sem acentos: ')
    rotacao = int(input('Informe a chave: '))
    vetorFrase = list(frase)
    
    for i in range(len(vetorFrase)):
        if vetorFrase[i].isalpha():
            valorCifra = ord(vetorFrase[i].lower()) - ord('a')
            novoValorCifra = (valorCifra + rotacao) % 26
            novaLetra = chr(ord('a') + novoValorCifra)
            vetorFrase[i] = novaLetra.upper() if vetorFrase[i].isupper() else novaLetra
    return ''.join(vetorFrase)

print(codificador())

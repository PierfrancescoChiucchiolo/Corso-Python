'''
comprimi stringhe con caratteri consecutivi: aaabbbcc -> a3b3c2
se la stringa non è più piccola della sua versione estesa allora restituisci l'originale

'''

'''
def compressor(stringa):

    appoggio = ''
    lista = []
    for index in range(len(stringa)):
        if index+1 <= len(stringa):
            if stringa[index] not in appoggio:
                lista.append(stringa[index])
                appoggio += "1"
            else:
                appoggio[index] = str( int(appoggio[index]) + 1 )
    if len(appoggio) < len(stringa):
        return appoggio
    else:
        return stringa
'''

def compressor(stringa):

    copy = list(stringa)
    appoggio = []




input1 = input("Dammi una stringa")
print(compressor(input1))
        

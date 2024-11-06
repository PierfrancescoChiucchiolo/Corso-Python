'''

creare una classe base MetodoPagamento e diverse classi derivate che rappresentano
diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in
azione, permettendo alle diverse sottoclassi di implementare i loro specifici
comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe
base.



Classe MetodoPagamento:
Metodi:
effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:
CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta
di credito.
PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite
bonifico bancario.
GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza
preoccuparsi del dettaglio del metodo di pagamento.


metodo di pagamento(iban, saldo):
metodo: effettua pagamento(importo)

carta di credito (titolare, iban) / paypal (username, iban) / bonifico(titolare, iban):
metodo: effettua pagamento(importo)

gestore pagamenti:
metodo: paga(metodo di pagamento, importo)

'''



class mdp():
    def __init__(iban, saldo):
        self._iban_ = iban
        self._saldo_ = saldo

    def __get_iban__(self):
        return self._iban_
    
    def __get_saldo__(self):
        return self._saldo_
    
    def __set_saldo__(self, importo):
        self._saldo_ = importo




class CDC(mdp):
    def __init__(iban, saldo, titolare):
        super().__init__(iban, saldo)
        self.titolare = titolare


class Paypal(mdp):
    def __init__(iban, saldo, username):
        super().__init__(iban, saldo)
        self.username = username


class Bonifico(mdp):
    def __init__(iban, saldo, titolare):
        super().__init__(iban, saldo)
        self.titolare = titolare


class Gestore_Pagamenti():
    def __init__(self, nome):
        self.nome = nome


    def paga(self, origine, destinazione, importo):
        if origine.__get_saldo__ >= importo:
            origine.__set_saldo__(origine.__get_saldo__() - importo)
            destinazione.__set_saldo__(destinazione.__get_saldo__() + importo)


gestore1 = Gestore_Pagamenti("MyTransfer")

cdc1 = CDC(5000, "Gianni Morandi")
paypal1 = Paypal(1000, "GianMorand")
bonifico1 = Bonifico(500, "Gianni Morandi")

print(cdc1.__get_saldo__)
print(paypal1.__get_saldo__)
print(bonifico1.__get_saldo__)

gestore1.paga(cdc1, paypal1, 500)

print(cdc1.__get_saldo__)
print(paypal1.__get_saldo__)
print(bonifico1.__get_saldo__)

gestore1.paga(cdc1, bonifico1, 500)

print(cdc1.__get_saldo__)
print(paypal1.__get_saldo__)
print(bonifico1.__get_saldo__)

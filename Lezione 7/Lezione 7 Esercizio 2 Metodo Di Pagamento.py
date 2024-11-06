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
    def __init__(self, iban, saldo):
        self._iban_ = iban
        self._saldo_ = saldo

    def get_iban(self):
        return self._iban_
    
    def get_saldo(self):
        return self._saldo_
    
    def set_saldo(self, importo):
        self._saldo_ = importo




class CDC(mdp):
    def __init__(self, iban, saldo, titolare):
        super().__init__(iban, saldo)
        self.titolare = titolare


class Paypal(mdp):
    def __init__(self, iban, saldo, username):
        super().__init__(iban, saldo)
        self.username = username


class Bonifico(mdp):
    def __init__(self, iban, saldo, titolare):
        super().__init__(iban, saldo)
        self.titolare = titolare


class Gestore_Pagamenti():
    def __init__(self, nome):
        self.nome = nome


    def paga(self, origine, destinazione, importo):
        if origine.get_saldo() >= importo:
            origine.set_saldo(origine.get_saldo() - importo)
            destinazione.set_saldo(destinazione.get_saldo() + importo)


gestore1 = Gestore_Pagamenti("MyTransfer")

cdc1 = CDC("IT1234567890", 5000, "Gianni Morandi")
paypal1 = Paypal("IT1122334455", 1000, "GianMorand")
bonifico1 = Bonifico("IT1231231231", 500, "Gianni Morandi")

print(cdc1.get_saldo())
print(paypal1.get_saldo())
print(bonifico1.get_saldo())

gestore1.paga(cdc1, paypal1, 500)

print(cdc1.get_saldo())
print(paypal1.get_saldo())
print(bonifico1.get_saldo())

gestore1.paga(cdc1, bonifico1, 500)

print(cdc1.get_saldo())
print(paypal1.get_saldo())
print(bonifico1.get_saldo())

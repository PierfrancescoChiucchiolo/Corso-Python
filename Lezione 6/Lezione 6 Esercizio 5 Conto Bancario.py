'''
creare una classe ContoBancario che incapsula le informazioni di un conto e
fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare
l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al
saldo del conto.



Classe ContoBancario:
Attributi privati:
__titolare (stringa che rappresenta il nome del titolare del conto)
__saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
deposita(importo): aggiunge un importo al saldo solo se l'importo è
positivo.
preleva(importo): sottrae un importo dal saldo solo se ci sono fondi
sufficienti e l'importo è positivo.
visualizza_saldo(): restituisce il saldo corrente senza permettere la sua
modifica diretta.
Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi
(e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare,
applicando validazioni appropriate (e.g., il titolare deve essere una stringa
non vuota).

extra: metodo privato e usarlo dentro l'oggetto, vedendo che non viene accesso

'''

class ContoBancario():
    def __init__(self, titolare, saldo, IBAN):
        self._titolare_ = titolare
        self._saldo_ = saldo
        self.__iban__ = IBAN
    
    def is_valid(self):
        return(self._titolare_ != "" and self._saldo_ >= 0)

    def set_titolare(self, titolare):
        if titolare != "": self._titolare_ = titolare
        else: print("Titolare non valido")

    def set_saldo(self, saldo):
        if saldo < 0: self._saldo_ = saldo
        else: print("Saldo non valido")

    def __set_iban__(self, IBAN):
        ## faccio finta l'iban sia sempre valido
        self.__iban__ = IBAN

    def get_titolare(self):
        return self._titolare_
    
    def get_saldo(self):
        return self._saldo_
    
    def __get_iban__(self):
        return self.__iban__

    def basta(self, importo):
        return self._saldo_ >= importo
    
    def deposita(self, importo):
        if self.is_valid() == False: print("Non valido")
        else:
            self._saldo_ += importo
            print("Deposito di " + str(importo) + " avvenuto con successo")
    
    def preleva(self, importo):
        attuale = self.get_saldo()
        print(attuale)
        if self.is_valid():
            if self.basta(importo):
                self._saldo_ = self._saldo_ - importo
        else: print ("Importo troppo elevato")


    def __cambia_iban__(self, IBAN):
        if self.__get_iban__ != IBAN:
            self.__set_iban__ == IBAN


conto1 = ContoBancario("Giovanni Giovannelli", 500, "IT1234567890")
print(conto1.get_titolare)
print(conto1.get_saldo)
conto1.preleva(1000)
print(conto1.get_saldo)

conto1.deposita(500)
print(conto1.get_saldo)

print(conto1.basta(500))
print(conto1.basta(1000))
print(conto1.basta(1500))

conto1.preleva(1000)
print(conto1.get_saldo)


print(conto1.__get_iban__)
conto1.__cambia_iban__("IT1122334455")
print(conto1.__get_iban__)

ContoBancario.__set_iban__(conto1, "IT1231231231")
print(conto1.__get_iban__)
print(conto1.__iban__)
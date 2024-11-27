'''
creare una classe base Posto che rappresenta un singolo posto nel teatro. Da questa, deriveranno
diverse classi per tipi specifici di posti, come PostoVIP e PostoStandard. Sarà inoltre

Classe Posto:
Attributi privati:
_numero (intero: numero del posto)
_fila (stringa: fila in cui si trova il posto)
_occupato (booleano: stato del posto, se è occupato o meno)
Metodi:
prenota(): prenota il posto se non è già occupato.
libera(): libera il posto se è occupato.
Getter per numero e fila, e uno stato che indica se il posto è occupato.
Classi Derivate:
PostoVIP:
Aggiunge un attributo per servizi_extra (e.g., accesso al lounge, servizio in posto).
Sovrascrive il metodo prenota() per includere la gestione dei servizi extra.
PostoStandard:
Potrebbe avere un costo aggiuntivo per la prenotazione online o altri servizi meno
esclusivi.
Classe Teatro:
Attributi:
_posti: lista di tutti i posti nel teatro.
Metodi:
prenota_posto(numero, fila): trova e prenota un posto specifico.
stampa_posti_occupati(): mostra tutti i posti occupati.



posto a teatro, posto vip / standard / teatro

posto: _numero / _fila / _occupato
metodi: prenota() / libera() / get numero e fila

posto vip: servizi extra / prenota() sovrascritto con servizi extra
posto standard: costo aggiuntivo online?

teatro: _posti
metodi: prenota(numero, fila) / stampa_occupati

'''


class Posto():
    def __init__(self, numero, fila, occupato = False):
        self._numero_ = numero
        self._fila_ = fila
        self._occupato_ = occupato

    def __get_numero__(self):
        return self._numero_
        
    def __get_fila__(self):
        return self._fila_
    
    def __get_occupato__(self):
        return self._occupato_
    
    def prenota(self):
        self._occupato_ = True

    def libera(self):
        self._occupato_ = False

    def dettagli(self):
        stringa = "Il posto è il numero: " + str(self._numero_) + " nella fila: " + str(self._fila_)
        return stringa

class PostoStandard(Posto):
    def __init__(self, numero, fila, occupato=False, online = False):
        super().__init__(numero, fila, occupato)
        self.online = online
    
    def get_online(self):
        return self.online
    
    def prenota(self, online):
        super().prenota()
        self.online = online
    
    def dettagli(self):
        stringa = super().dettagli()
        if self.get_online(): stringa + " e il posto è stato prenotato online"
        return stringa
    
class PostoVIP(Posto):
    def __init__(self, numero, fila, occupato=False, extra = ""):
        super().__init__(numero, fila, occupato)
        self.extra = extra

    def has_extra(self):
        return self.extra == ""

    def get_extra(self):
        return self.extra
    
    def prenota(self, servizi):
        super().prenota()
        self.extra = servizi

    def dettagli(self):
        stringa = super().dettagli()
        if self.has_extra():
            servizi = self.extra
            
            stringa = stringa + " e il posto è stato prenotato con i servizi extra: " + servizi
        return stringa


class Teatro():
    def __init__(self, nome, indirizzo, righe, colonne):
        self.nome = nome
        self.indirizzo = indirizzo
        self.righe = righe
        self.colonne = colonne
        self.capienza = righe * colonne
        self.posti = {}

    def check_capienza(self):
        return self.capienza - len(self.posti)
    
    def check_prenotabile(self, numero, fila):
        if not self.check_capienza(): return False
        elif numero > self.righe or fila > self.colonne: return False
        elif (numero, fila) in self.posti.keys(): return False
        else: return True 
    
    def prenota_standard(self, numero, fila, online = 0):
        if self.check_prenotabile(numero, fila):

            standard = PostoStandard(numero, fila, online)
            standard.prenota(online)
            nuovo_posto = {(numero, fila) : standard}
            self.posti.update(nuovo_posto)

    def prenota_vip(self, numero, fila, servizi = ""):
        if self.check_prenotabile(numero, fila):

            vip = PostoVIP(numero, fila, servizi)
            vip.prenota(servizi)
            nuovo_posto = {(numero, fila) : vip}
            self.posti.update(nuovo_posto) 

    def stampa_occupati(self):
        for posto in self.posti.values():
            print(posto.dettagli())

    
teatro1 = Teatro("Teatro delle Vittorie", "Parco della Vittoria 1", 2, 2)

print(teatro1.check_capienza())
teatro1.prenota_standard(1, 1, 0)
teatro1.prenota_vip(2, 2, "Nessuno")
teatro1.stampa_occupati()
print(teatro1.check_capienza())


print("provo a prenotare 1, 1 già occupato")
teatro1.prenota_standard(1, 1, 0)

print("provo a prenotare altri 2 posti alla capienza di 4 posti")
teatro1.prenota_standard(2, 1, 1)
teatro1.prenota_vip(1, 2, "Poltrona massaggiante")
print(teatro1.check_capienza())

teatro1.stampa_occupati()


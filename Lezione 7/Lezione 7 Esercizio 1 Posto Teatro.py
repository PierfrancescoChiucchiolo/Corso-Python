'''
creare una classe base Posto che rappresenta un singolo posto nel teatro. Da questa, deriveranno
diverse classi per tipi specifici di posti, come PostoVIP e PostoStandard. Sarà inoltre
necessaria una classe Teatro per gestire tutti i posti e le prenotazioni.

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
import copy

from database import meteo_dao

class Model:
    def __init__(self):
        self._soluzione = []
        self._daPrintare = []

    def medie(self, mese):
        lista = meteo_dao.MeteoDao.valoriMedi(mese)
        return lista

    def confronta(self, soluzione1, soluzione2, mese):
        daPrintare1 = []
        daPrintare2 = []
        somma1 = 0
        somma2 = 0
        s = 1
        for i in range(len(soluzione1)):
            if i!=0 and soluzione1[i] != soluzione1[i-1]:
                somma1= somma1+100
            for j in range(3):
                umidita, data = meteo_dao.MeteoDao.tornaUmidita(mese,s, soluzione1[i])
                s = s+1
                daPrintare1.append(f"{data}, {soluzione1[i]}, {umidita}")
                somma1 = somma1+ umidita
        s = 1
        for x in range(len(soluzione2)):
            if x!=0 and soluzione2[x] != soluzione2[x-1]:
                somma2 = somma2+100
            for k in range(3):
                umidita, data = meteo_dao.MeteoDao.tornaUmidita(mese,s, soluzione2[x])
                s = s+1
                daPrintare2.append(f"{data}, {soluzione2[x]}, {umidita}")
                somma2 = somma2+ umidita
        if somma1<somma2:
            self._daPrintare= []
            self._daPrintare.append(somma1)
            self._daPrintare.extend(daPrintare1)
            return soluzione1
        else:
            self._daPrintare = []
            self._daPrintare.append(somma2)
            self._daPrintare.extend(daPrintare2)
            return soluzione2

    def ricursione(self, mese, parziale, listaCitta, dizionarioCitta, giorno):
        if giorno == 15:
            if self._soluzione == []:
                self._soluzione = copy.deepcopy(parziale)
            else:
                self._soluzione = self.confronta(self._soluzione, parziale, mese)
        elif giorno>15:
            return
        else:
            giorno1 = giorno +3
            for element in listaCitta:
                if dizionarioCitta[element] <=3:
                    dizionarioCitta1 = copy.deepcopy(dizionarioCitta)
                    dizionarioCitta1[element] = dizionarioCitta[element] + 3
                    parziale1 = copy.deepcopy(parziale)
                    parziale1.append(element)
                    self.ricursione(mese, parziale1, listaCitta, dizionarioCitta1, giorno1)

    def esegui(self, mese):
        self._soluzione = []
        listaCitta = ["Milano", "Torino", "Genova"]
        dizionarioCitta = {}
        for element in listaCitta:
            dizionarioCitta[element] = 0
        parziale = []
        self.ricursione(mese, parziale, listaCitta, dizionarioCitta, 0)
        return self._daPrintare



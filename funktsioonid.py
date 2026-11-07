import yfinance as yf # Impordib Yahoo Finance'i teegi, et saaksime aktsiaandmeid alla laadida.
import pandas as pd # Impordib Pandas teegi, et saaksime andmeid töödelda ja analüüsida.
import matplotlib.pyplot as plt # Impordib Matplotlib teegi, et saaksime andmeid visualiseerida.

def laadi_andmed(tähis, algus, lõpp): # Defineerib funktsiooni parmeetritega tähis, algus, lõpp.
    try: # Alustab veakäsitlust, et programm ei katkeks vea tekkimisel.
        andmed = yf.download( # Laeb valitud aktsia andmed tabelina alla.
            tähis, # Määrab, milise aktsia andmeid soovitakse.
            start=algus, # Määrab andmete alguskuupäeva.
            end=lõpp, # Määrab andmete lõppkuupäeva.(See päev ise hulka ei kuulu.)
            auto_adjust=True, # Korrigeerib andmeid, avrestades dividendide ja aktsiasplittide mõju
            progress=True # Näitab terminalis kasutajale allalaadimise edenemist.
        )

        if andmed.empty: # Kontrollib, kas allalaaditud tabel on tühi, mis tähendab, et eandmeid ei leitud.
            raise ValueError("Aktsia andmeid ei leitud.") # Tekitab vea, kui andmeid ei leitud.

        return andmed # Tagastab allalaaditud andmed.
    except Exception as viga:
        print("Andmete laadimisel tekkis viga ", viga)
        return None
def liikuv_keskmine(hinnad, n):     #hinnad on hindade järjend, n on paevade arv
    tulemus = []                    #järjend, kuhu salvestatakse liikuvate keskmiste väärtused
    for i in range(len(hinnad)):    #tsükkel, et luua keskmiste järjend
        if i >= n - 1:              #n-1, sest esimene liikuv keskmine saab tekkida alles siis, kui on olemas n väärtust ning indeksid algavad 0-st
            arit = float(sum(hinnad[i + 1 - n:i + 1]) / n)        #summa n väärtusest õiges vahemikus, jagatud n-ga, i + 1, sest i on indeks, mis algab 0-st
            tulemus.append(arit)      #lisame arvutatud keskmise tulemuste järjendisse
        else:
            tulemus.append(None)        #kui liikuv keskmine ei ole võimalik, lisame None, et järjend säilitaks oma pikkuse
    return tulemus                      #funktsioon tagastab liikuvate keskmiste järjendi


def signaalid(MAx, MAy):    #MAx on pikema perioodi keskmiste jarjend, MAy on lühema perioodi keskmiste jarjend, mõlemad on endiselt hinnad järjendiga sama pikkused
    signaalid = [None]      #järjend, kuhu salvestatakse signaalid, alguses None, sest päeval 0 signaali ei saa olla, sest pole eelmist päeva
    eelmine = None          #muutuja, mis salvestab eelmise signaali oleku, et seda järgmisega võrrelda ja potentsiaalne üleminek tuvastada, alguses None, sest i - 1 korral tuleks i = -1 ning alguses pole varasemaid olekuid teada

    for i in range(1, len(MAx)):
        if MAx[i-1] is None:        #kontrollib, kas eelmine liikuv keskmine on None, kui on, siis ei saa teda järgmisega võrrelda, seega lisame None signaalide järjendisse ja jätkame järgmise iteratsiooniga
            signaalid.append(None)
            continue

        if MAx[i-1] is not None: #kuna esimese sobiva keskmise korral pole muutujale eelmine veel eelmise olekut, siis määrame selle vastavalt sellele, kas MAx on suurem või väiksem kui MAy
            if MAx[i-1] > MAy[i-1]:    
                eelmine = 'all'
            elif MAx[i-1] < MAy[i-1]:
                eelmine = 'yleval'
            else:
                eelmine = 'neutral'

        if MAx[i] == MAy[i]:        #kuigi võrdus on ujukomadega praktiliselt võimatu, pidasin vajalikuks selle lisada, et vältida ka ebatõenäolistes olukordades vigu ja vale signaalide genereerimist, kui tegu on vaid puutega
            signaalid.append('neutral')
            continue
        else:
            if MAx[i] > MAy[i]:     #kui erandid on kontrollitud, siis määrame oleku
                olek = 'all'
            else:
                olek = 'yleval'

        if eelmine == 'all' and olek == 'yleval':   #võrdleme eelmist ja praegust olekut, et tuvastada üleminekud
            signaalid.append('buy')
        elif eelmine == 'yleval' and olek == 'all':
            signaalid.append('sell')
        elif eelmine == 'neutral':                  #juhul, kui eelmine olek oli võrdne, kontrollime üle-eelmist päeva, et eristada ristumist puutest
            if olek == 'all':
                if i >= 2 and MAx[i-2] is not None and MAx[i-2] > MAy[i-2]:
                    signaalid.append(None)
                else:
                    signaalid.append('sell')
            else:
                if i >= 2 and MAx[i-2] is not None and MAx[i-2] < MAy[i-2]:
                    signaalid.append(None)
                else:
                    signaalid.append('buy')

        else:       #kui üleminekut ei toimu ehk praegune on ikka eelmisest all/üleval, siis lisame None, et järjend säilitaks oma pikkuse
            signaalid.append(None)

        eelmine = olek      #omistame muutujale eelmine praeguse oleku, et seda järgmise iteratsiooni puhul võrrelda
    return signaalid        #funktsioon tagastab signaalide järjendi, mis on sama pikk kui sisendjärjendid

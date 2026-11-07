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

    except Exception as viga: # Käsitleb kõiki vigu, mis võivad tekkida andmete allalaadimisel.
        print("Andmete laadimisel tekkis viga: ", viga) # Kuvab kasutajale vea põhjuse.
        return None # Tagaastab None, kui andmete laadimine ebaõnnestus.
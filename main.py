from funktsioonid import laadi_andmed, liikuv_keskmine, signaalid # Impordib funktsioonid

def main():
   
    tähis = input("Sisesta aktsia sümbol (näiteks AAPL, MSFT): ") # Küsib kasutajalt aktsia tähist.
    algus = input("Sisesta alguskuupäev (AAAA-KK-PP): ") # Küsib kasutajalt alguskuupäeva.
    lõpp = input("Sisesta lõppkuupäev (AAAA-KK-PP): ") # Küsib kasutajalt lõppkuupäeva.
    
    andmed = laadi_andmed(tähis, algus, lõpp) # Kutsub välja funktsiooni andemte allalaadimiseks.

    if andmed is None:
        return # Kui laadimine ebaõnnestus, lõpetab programmi töö.

    hinnad = andmed["Close"].squeeze().tolist() # Võtab tabelist sulgemishinnad ja teeb nendest järjendi.
    lühike_n = int(input("Sisesta lühiajalise liikuva keskmise periood (naturaalarv, nt. 20): ")) # Küsib kasutajalt lühiajalise liikuva keskmise perioodi.
    pikk_n = int(input("Sisesta pikaajalise liikuva keskmise periood (naturaalarv, nt. 50): ")) # Küsib kasutajalt pikaajalise liikuva keskmise perioodi.

    lühike_keskmine = liikuv_keskmine(hinnad, lühike_n) # Arvutab lühiajalise liikuva keskmise.
    pikk_keskmine = liikuv_keskmine(hinnad, pikk_n) # Arvutab pikaajalise liikuva keskmise.

    tulemused = signaalid(pikk_keskmine, lühike_keskmine) # Arvutab signaalid lühikese ja pika liikuva keskmise põhjal.

    signaal_leitud = False # Muutuja väärtusega False, mis näitab, et signaale pole.
    for i in range(len(tulemused)): # Käib tulemused indeksi põhjal läbi
       kuupäev = andmed.index[i] # Võtab vastava kuupäeva
       signaal = tulemused[i] # Võtab vastava signaali
       if signaal == "buy": # Kontrollime, kas signaal on ostusignaal.
            print(f"{kuupäev.strftime('%Y-%m-%d')}: Osta") #strftime() vormindab kuupäeva.
            signaal_leitud = True # Märgib, et kuupäev leiti.
       elif signaal == "sell": # Kui ostusignaal polnud, kontrollime müügisignaali.
            print(f"{kuupäev.strftime('%Y-%m-%d')}: Müü") #strftime() vormindab kuupäeva.
            signaal_leitud = True # Märgib, et kuupäev leiti.

    if not signaal_leitud: # Kui signaali ei leitud, väljastab teate.
        print("Antud ajavahemikus signaale ei leitud.") # Kui signaale ei leitud, kuvab teate.

if __name__ == "__main__":
    main() # Käivitab programmi peamise funktsiooni 

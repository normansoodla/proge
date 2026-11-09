# Aktsiahinna analüüs

## Projekti kirjeldus

Projekt on Pythoni programm, mis võimaldab analüüsida aktsiate ajaloolisi hinnaandmeid liikuvate keskmiste abil. Programm kasutab Yahoo Finance'i andmeid, et uurida aktsiate hinnaliikumisi ning neist järeldada võimalikke ostu- ja müügisignaale.

Programmi abil saab kasutaja valida analüüsitava aktsia ja ajavahemiku ning tutvuda analüüsi tulemustega.

## Projekti eesmärk

Projekti eesmärk on õppida kasutama Pythonit finantsandmete töötlemiseks ja analüüsimiseks ning luua tööriist aktsiahindade analüüsimiseks.

## Programmi töö

- Analüüsitava aktsia määramine.
- Ajavahemiku määramine, mille ajal aktsia hindu uuritakse.
- Aktsia ajalooliste hinnaandmete Yahoo Finance'ist alla laadimine.
- Aktsia hindade põhjal liikuvate keskmiste arvutamine.
- Liikuvate keskmiste võrdlemise tulemusel, võimalike ostu- ja müügisignaalide tuvastamine.
- Analüüsi tulemuste kasutajale esitamine.
- Aktsia ajalooliste hindade, liikuvate keskmiste ja tuvastatud signaalide graafikul kujutamine.

## Failide kirjeldus

- "README.md" - projekti tutvustus.
- "main.py" - programmi käivitamine, kasutajalt sisendi küsimine ja funktsioonide töö korraldamine.
- "funktsioonid.py" - programmis kasutatavad funktsioonid: andmete laadimine, liikuvate keskmiste arvutamine, signaalide tuvastamine ja graafiku loomine.
- "requirements.txt" - projektis kasutatavate Pythoni teekide loend.
- ".gitignore" - failid ja kaustad, mida ei lisata GitHubi repositooriumisse.

## Programmi käivitamisjuhend

Programmi kasutamiseks peab arvutis olema paigaldatud Python.
1. Laadi porjekt Githubist alla või klooni see enda arvutisse.
2. Ava Powershell või muu terminal ja liigu projekti kausta.
3. Paigalda vajalikud teegid käsuga:

```bash
python -m pip install -r requirements.txt
```

4. Käivita programm käsuga:

```bash
python main.py
```
5. Sisesta programmi küsitavad andmed.

## NB!

Programmi tuvastatud ostu- ja müügisignaalid tulenevad vanade andmete analüüsist. Need ei taga tulevikus tootlust ega kujuta endast investeerimissoovitusi.

## Projekti autorid

Norman Soodla, Karl Oskar Veidebaum

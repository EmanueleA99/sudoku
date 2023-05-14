# Challenge 1: Hexadoku

**<u>Consegna: 20 novembre 2019</u>**

## Challenge Algoritmico: regole generali

* Durante il corso, verranno pubblicati tre problemi da risolvere
* Gli studenti possono consegnare (entro scadenze prestabilite) dei programmi che risolvono questi problemi
* I programmi verranno testati sugli input di prova forniti agli studenti e su altri input utilizzati unicamente per testare la correttezza
* I programmi corretti verranno organizzati in una graduatoria, in funzione della loro efficienza
  I primi tre classificati riceveranno 2 punti in più che verranno sommati al voto finale
* Si può totalizzare un massimo di 4 punti con la Challenge
* I punti scadono al termine dell'anno accademico

**ATTENZIONE**: verrà effettuato un **controllo automatico antiplagio**. I programmi che verranno classificati dal sistema di controllo come *copiati* (o "fortemente ispirati") ad altri programmi inviati nella challenge o trovati su repository online verranno scartati dalla graduatoria finale.

## Descrizione del problema

L'**hexadoku** è un sudoku su una griglia 16 x 16, anziché 9 x 9. I principi di risoluzione sono equivalenti a quelle di un classico sudoku, ma vengono utilizzate le cifre del **sistema esadecimale**. Un esempio di griglia è riportata qui di seguito.

![hexadoku](https://i.pinimg.com/originals/fe/bb/3f/febb3f765793262170c52beeb7c91247.jpg)

La griglia ha dimensione 16 x 16 ed è divisa i 16 sottogriglie denominate **regioni** (evidenziate con i bordi più spessi sulla griglia). Il problema in input ha alcune caselle che contengono già dei numeri. Per identificare la soluzione è necesario riempire le celle vuote con numeri tra l’`1` ed `F` (un solo numero per cella) rispettando questi vincoli:

* Un numero può apparire solo una volta per riga
* Un numero può apparire solo una volta per colonna
* Un numero può apparire solo una volta per regione

## Input/output

Vengono fornite due griglie di esempio con cui effettuare i test, all'interno della sottocartella `input/`. I file sono in formato `csv` (comma separated values). È possibile utilizzare la libreria `csv` di python per caricare in memoria il contenuto di questo file e per salvare su file il risultato della griglia. Si faccia riferimento alla [documentazione](https://docs.python.org/3/library/csv.html) per informazioni aggiuntive.

Lo script in python deve accettare un percorso alla griglia come primo ed unico argomento. La soluzione al problema deve essere scritta su un file chiamato `soluzione.csv`.

## Cosa consegnare

Deve essere presente un file `main.py` che costituisce il punto di ingresso del risolutore. È possibile importare in questo script qualsiasi script aggiuntivo necessario ad implementare il risolutore. All'interno dello scheletro di `main.py` presente in questo repo è indicata la versione 3 di Python. Qualora lo studente volesse implementare il risolutore con la versione 2 di Python, è necessario aggiornare la prima riga di quel file.

Il file `Informazioni.md` deve essere compilato con le informazioni sullo studente, pena la perdita del bonus.

È sufficiente aggiungere il codice alla propria copia del repository. Il docente recupererà l'implementazione presente nell'ultimo commit alla scadenza della consegna.

## Termine di consegna

Il termine di consegna è il **20 novembre 2019**. Alla mezzanotte di quella data, tutti i repository verranno "congelati" e verrà testata l'implementazione presente nell'ultimo commit.
Oppgave 3: Databehandling

Oppgave 3 går ut på å strukturere, rense og klargjøre dataene for videre analyser, med spesielt fokus på håndtering av manglende verdier og uregelmessigheter. Vi har benyttet verktøy som pandas, pandasql, list comprehensions og iteratorer for å gjennomføre databehandlingen på en effektiv og oversiktlig måte. 

Vi ønsket å estimere CO₂-utslipp fra lakseeksport. Dataene fra SSB inneholder hverken informasjon om transportmiddel eller destinasjon. For å kunne utføre ulike miljødataanalyser med våre data som utgangspunkt, er vi derfor nødt til å gjøre realistiske antagelser. 
For å kunne gjøre dette antar vi at fersk laks fraktes med fly (1.1 kg CO₂ per tonn-km, 2000 km) og frosset laks med skip (0.01 kg CO₂ per tonn-km, 5000 km). Disse estimatene gir et grovt men illustrativt bilde av transportrelaterte utslipp. Dette estimatet er ikke 100% presist, men gir en god indikasjon på miljøpåvirkningen over tid. Ved å gjøre disse realistiske antagelsene kan vi analysere trender og utvikling.

Håndtering av manglende verdier
Datasettet inneholder uker der det ikke er registrert eksport av hverken fersk eller frosset laks. For å sikre meningsfulle analyser fjernet vi rader med manglende eksportvekt. Selv om datasettet i utgangspunktet ikke hadde nullverdier, har vi inkludert kode som identifiserer og filtrerer bort manglende data ved bruk av .isnull() og .dropna(). 
Vi simulerte også feil ved å legge inn tilfeldige og målrettede NaN-verdier for å teste hvor robust dataene var (bl.a. 2000 i kolonnen "Fersk laks – Kilospris" i datarensing_nullverdier filen). Disse ble fjernet og gjenopprettet via fillna() basert på en kopi av det opprinnelige datasettet. Dette demonstrerte hvor viktig datarensing er for å oppnå nøyaktige resultater, og illustrerer hvordan datakvalitet kan påvirkes av manglende rapportering og systemfeil.
Dette er viktig for å sikre robusthet ved fremtidige kjøringer eller utvidelser av datasettet.

I visualiseringen ser vi tydelig at datasettet med feil gir en mer hakkete og ujevn kurve, mens det gjenopprettede datasettet fremstår glatt og konsistent. Dette demonstrerer hvordan effektiv bruk av Pandas-metoder kan forbedre datakvaliteten og gjøre analysen mer pålitelig.
Man kunne brukt median for å fylle tilbake tapte verdier, men vi valgte å ikke gjøre det fordi vi har verdiene fra originaldataen.


Identisfisering av tapte verdier i et datasett kan man bruke Pandas biblioteket, som da gir tilbake om datasettet har null-verdier. Her vil koden returnere og dataen er falsk eller sann for om verdiene er nullverdier. Det er også mulig å fjerne rader med null-verdier, eller ta et gjennomsnitt av verdien over og under null-verdien og legge inn det istedenfor null-verdien.
Man bruker .isnull() funksjonen fra Pandas for å sjekke om verdiene du får er null-verdier. Det kommer True der det er null-verdier og False der verdiene er korrekte tall. https://www.geeksforgeeks.org/python-pandas-isnull-and-notnull/ 
Siden det ikke var noen null-verdier har det vært mulig å legge inn tilfeldige nullverdier I hver kolonne. Det går an å justerer hvor ofte man vil dette skal skje, det er 10 % som er lagt inn som frekvens i koden. 
Jeg har brukt .isnull() og .dropna() funksjoner for å isdentifisere null-verdi rader og deretter fjerne dem. Etter dette har jeg brukt dette datasettet som er renset til å visualisere resultatet over fersk og frossen laks i en graf.



Bruk av list comprehensions
List comprehensions ble brukt for å trekke ut og kombinere verdier fra den komplekse og hierarkiske JSON-strukturen i API-et. Dette gjorde databehandlingen både raskere og mer lesbar. Dette gjorde det mer effektivt å bygge en fullstendig datastruktur med ulike kombinasjoner av av laksetype og måleenhet.

For eksempel har vi brukt lambda og apply() til å lage kolonner for pris- og vektklassifisering, der vi kategoriserte laks som "billig", "normal" eller "dyr" basert på gitte grenseverdier. Vi bestemte at alt over 90 kr er dyrt, prisen over medianprisen er normal (45 kr), og resten er billig. 



Bruk av Pandas SQL (sqldf)
Selv om pandas har kraftige funksjoner for aggregering og gruppering, har vi valgt å benytte pandasql for å utføre deler av datamanipuleringen. Dette gir muligheten til å bruke SQL-syntaks direkte på pandas-data, noe som gjør enkelte operasjoner — som gruppering og summering — enklere å skrive og lese, særlig for dem som er vant til SQL. Dette gir bedre lesbarhet og struktur når man for eksempel skal oppsummere CO₂-utslipp per uke og laksetype.

Håndtering av uregelmessigheter i dataene
Datasettet inneholder enkelte uregelmessigheter som må håndteres. En utfordring vi støtte på allerede ved datainnsamlingen i oppgave 2, er variasjoner i navngivning – for eksempel at “frosset laks” kan oppgis med små variasjoner i tekst som: “frosen oppalen laks” i datasettet til SSB. For å håndtere dette har vi brukt tekstfiltrering og standardisering, slik at transporttypene alltid kategoriseres som enten "Fersk laks" eller "Frosset laks". 
I tillegg tar vi høyde for at eksporttall for inneværende år (2025) ofte er ufullstendige, og derfor bør utelates fra videre analyser, eksempelvis predikasjon. 

Konklusjon
Gjennom systematisk bruk av verktøy som pandas, pandasql, list comprehensions og datarensingsteknikker har vi behandlet ukentlig eksportdata fra SSB på en strukturert og robust måte. Vi har sikret at datasettene vi analyserer er rene, konsekvente og klargjort for videre analyser i del 2, som prediksjon og visualisering. Denne formen for databehandling danner et viktig grunnlag for pålitelige og relevante innsikter i det videre arbeidet med dataene.

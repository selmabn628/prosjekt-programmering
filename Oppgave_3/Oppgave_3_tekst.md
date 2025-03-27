Oppgave 3: Databehandling

Oppgave 3 går ut på å strukturere, rense og klargjøre dataene for videre analyser, med spesielt fokus på håndtering av manglende verdier og uregelmessigheter. Vi har benyttet verktøy som pandas, pandasql, list comprehensions og iteratorer for å gjennomføre databehandlingen på en effektiv og oversiktlig måte. 

Vi ønsket å estimere CO₂-utslipp fra lakseeksport. Dataene fra SSB inneholder hverken informasjon om transportmiddel eller destinasjon. For å kunne utføre ulike miljødataanalyser med våre data som utgangspunkt, er vi derfor nødt til å gjøre realistiske antagelser. 
For å kunne gjøre dette antar vi at fersk laks fraktes med fly (1.1 kg CO₂ per tonn-km, 2000 km) og frosset laks med skip (0.01 kg CO₂ per tonn-km, 5000 km). Disse estimatene gir et grovt men illustrativt bilde av transportrelaterte utslipp. Dette estimatet er ikke 100% presist, men gir en god indikasjon på miljøpåvirkningen over tid. Ved å gjøre disse realistiske antagelsene kan vi analysere trender og utvikling.

Håndtering av manglende verdier
Datasettet kan inneholde noen uker der det ikke er registrert eksport av hverken fersk eller frosset laks. For å sikre at analysene baserer seg på meningsfulle og komplette datapunkter, har vi fjernet rader som mangler informasjon om eksportert vekt. Ved å gjøre dette unngår vi at analyser og beregninger baserer seg på tomme eller ufullstendige verdier. 
Selv om det ikke ble funnet manglende verdier i dette datasettet, har vi implementert kode som identifiserer og filtrerer bort ufullstendige rader. Dette er viktig for å sikre robusthet ved fremtidige kjøringer eller utvidelser av datasettet.

Bruk av list comprehensions
For å behandle den komplekse og hierarkiske JSON-strukturen vi får fra SSB sitt API, har vi brukt list comprehensions til å hente ut og kombinere verdiene fra flere dimensjoner. Dette gjør det mulig å effektivt bygge opp en fullstendig datastruktur med alle relevante kombinasjoner av uke, laksetype og måleenhet. Det gjør prosessen mer effektiv og lesbar enn alternative løsninger med løkker.

Ved bruk av Lambda funksjoner kan man manipulerer dataene
Ved bruk av “apply” funksjonen når man bruker lambda kan man eksempelvis legge til to nye kolonner med nye verdier, her har jeg lagt til nye kolonner for kilopris og vekt av fersk laks. 
Videre har jeg valgt å bruke en lambda funksjon til å lage en if-setning som sier noe om laksen er dyr eller billig. Her har jeg bestemt at alt over 90 kr er dyrt, prisen over medianprisen er normal (45 kr), og resten er billig. 


Bruk av Pandas SQL (sqldf)
Selv om pandas har kraftige funksjoner for aggregering og gruppering, har vi valgt å benytte pandasql for å utføre deler av datamanipuleringen. Dette gir muligheten til å bruke SQL-syntaks direkte på pandas-data, noe som gjør enkelte operasjoner — som gruppering og summering — enklere å skrive og lese, særlig for dem som er vant til SQL. Dette gir bedre lesbarhet og struktur når man for eksempel skal oppsummere CO₂-utslipp per uke og laksetype.

Håndtering av uregelmessigheter i dataene
Datasettet inneholder enkelte uregelmessigheter som må håndteres. En utfordring vi støtte på allerede ved datainnsamlingen i oppgave 2, er variasjoner i navngivning – for eksempel at “frosset laks” kan oppgis med små variasjoner i tekst (som “frosen oppalen laks” i datasettet til SSB). For å håndtere dette har vi brukt tekstfiltrering og standardisering, slik at transporttypene alltid kategoriseres som enten "Fersk laks" eller "Frosset laks". 
I tillegg tar vi høyde for at eksporttall for inneværende år (2025) ofte er ufullstendige, og derfor bør utelates fra i videre analyser, eksempelvis predikasjon. 

Konklusjon
Gjennom systematisk bruk av verktøy som pandas, pandasql, list comprehensions og datarensingsteknikker har vi behandlet ukentlig eksportdata fra SSB på en strukturert og robust måte. Vi har sikret at datasettene vi analyserer er rene, konsekvente og klargjort for videre analyser i del 2, som prediksjon og visualisering. Denne formen for databehandling danner et viktig grunnlag for pålitelige og relevante innsikter i det videre arbeidet med dataene.

Databehandling:

I denne delen av prosjektet fokuserte vi på å forberede og rense dataene vi hentet fra Statistisk sentralbyrå (SSB), slik at de kunne brukes videre til analyse og visualisering. Vi brukte Pandas til å behandle JSON-data fra SSBs API, og gjorde nødvendige transformasjoner for å rydde opp i strukturen og sikre kvalitet i datasettet.

Først hentet vi data og gjorde dem om til en flat, lesbar tabell med hjelp av itertools.product og pivot_table i Pandas. Deretter delte vi opp tidspunktene til år og uke for å gjøre det lettere å analysere og visualisere utvikling over tid. Vi la også til en UkeDato-kolonne, som automatisk regnet ut en dato for hver uke – noe som var nyttig for grafisk fremstilling.

For å demonstrere håndtering av manglende verdier, la vi inn både tilfeldige og målrettede NaN-verdier i datasettet. Dette simulerte feil som ofte kan oppstå i virkelige datakilder, som for eksempel manglende rapportering eller systemsvikt. Ved hjelp av funksjoner som .isnull() og .dropna() identifiserte vi og fjernet radene med manglende data, og med .fillna() klarte vi å gjenopprette verdiene fra en tidligere kopi av det originale datasettet. Dette viste oss hvordan datasett kan repareres etter skade, og hvilken påvirkning dette har på analysegrunnlaget.

Vi brukte også apply() med lambda-funksjoner til å legge til nye beregninger og klassifiseringer, for eksempel for å merke kiloprisene på fersk laks som "Billig", "Normal" eller "Dyr", avhengig av verdi. I tillegg ble det brukt list comprehensions for å trekke ut verdier fra JSON-strukturen, noe som gjorde koden både mer effektiv og lettere å lese.

Til slutt brukte vi visualisering til å vise forskjellen mellom det skadede og det gjenopprettede datasettet. Diagrammene viste tydelig hvordan manglende verdier førte til hakkete, uforutsigbare kurver, mens den rensede versjonen var jevn og konsistent. Dette understreket viktigheten av grundig datarensing før analyse.

Vi testet også hvordan pandasql kan brukes for å gjøre spørringer i datasettet med SQL-lignende syntaks. Selv om det ble brukt i begrenset grad her, ser vi hvordan det kan være nyttig for mer komplekse datastrukturer eller dersom man er vant til SQL fra før.

Gjennom denne oppgaven har vi fått god erfaring med å identifisere, rydde og transformere data, og vi har sett hvordan god databehandling er avgjørende for å få pålitelige og meningsfulle analyser.
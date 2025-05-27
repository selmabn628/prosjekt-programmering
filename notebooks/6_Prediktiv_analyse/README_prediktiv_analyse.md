Visualisering og prediktiv analyse:

I denne delen av prosjektet har vi brukt interaktive visualiseringer for å formidle innsikt fra lakseeksportdata over tid, og kombinert dette med en prediktiv modell for å forutsi fremtidig eksportverdi. Dataene er hentet fra SSBs API og supplert med en CSV-fil som inneholder årlig eksportverdi for fersk laks.

Vi har utviklet tre typer visualiseringer:

Linjediagram med dobbel y-akse som viser utviklingen i vekt (tonn) og kilopris (kr/kg) for fersk laks over tid. Dette gir et tydelig bilde av forholdet mellom volum og pris.
Linjediagram med tre y-akser som viser utviklingen i eksportverdi, vekt og kilopris parallelt. Her kombinerer vi API-data og CSV-data, og gjør det mulig å se hvordan markedsverdien påvirkes av endringer i volum og pris.
Regresjonsbasert prediksjonsgraf hvor vi benytter lineær regresjon til å forutsi fremtidig eksportverdi basert på forventet kilopris. Denne grafen illustrerer både historiske sammenhenger og predikert utvikling frem mot 2035, og gir dermed både innsikt og beslutningsstøtte.
Vi valgte interaktive grafer med Plotly fordi de gjør det lettere å utforske sammenhenger i tidssensitive data, spesielt når flere variabler skal vises samtidig. De doble og tredoble y-aksene gjør det mulig å sammenligne verdier med forskjellige størrelsesordener uten å miste presisjon i tolkningen.

Visualiseringene er støttet av dataforberedelse med Pandas. Vi hentet inn og transformerte datasettet, ekstraherte årstall fra datostrenger, og brukte .groupby().mean() til å aggregere årlige gjennomsnittsverdier. Vi sørget også for å rense datasettene, inkludert å fjerne rader med manglende verdier før modelltrening. Dette er viktig for å unngå at modellen forvrenges av ufullstendig informasjon. Ved bruk av .dropna() og .fillna() ble alle rader med NaN håndtert eksplisitt, og i analysen ble det tydelig at dette forbedret kvaliteten og nøyaktigheten i prediksjonene.

Vi brukte scikit-learn sin LinearRegression()-modell for å lære sammenhengen mellom kilopris og eksportverdi. Modellen ble trent på historiske data fra 2015–2024 og brukt til å predikere eksportverdi fra 2025–2035, basert på en konservativt estimert prisvekst. Resultatet ble plottet i et diagram hvor vi sammenligner predikert eksportverdi med historiske data, og den predikerte kurven gir et godt bilde av mulig fremtidig utvikling.

Ettersom eksportverdi-dataene var hentet fra CSV (og ikke et API), innebærer dette en viss risiko for at dataene kan være utdaterte. Dette ble også reflektert i kommentarene i koden og understreker viktigheten av å bruke API-er for kontinuerlig oppdatert analyse dersom modellen skal brukes operativt.

Evaluering:
De mest effektive visualiseringene viste seg å være de interaktive diagrammene med doble eller tredoble y-akser. Disse gjorde det enkelt å utforske sammenhenger og oppdage trender. Tilbakemeldinger fra medstudenter viste at disse diagrammene var lette å lese og ga et godt overblikk, særlig fordi de integrerte både økonomiske og fysiske aspekter av lakseeksport.
Sammenlignet med enklere linjediagrammer fra tidligere oppgaver, ga Plotly-diagrammene et mer profesjonelt preg og høyere informasjonsverdi.

Gjennom denne delen fikk vi erfaring med både datafusjon, regresjonsmodellering og visuell formidling, som samlet har gjort prosjektet mer robust og innsiktsfullt.
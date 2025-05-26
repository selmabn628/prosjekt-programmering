Oppgave 4: Dataanalyse	

I denne delen av prosjektet har vi brukt verktøy som Pandas, NumPy og Matplotlib for å analysere sammenhengen mellom valutakurs og eksportpriser på laks. Formålet har vært å identifisere trender, variasjoner og mønstre i prisutviklingen for fersk og frosset laks over tid, samt undersøke hvordan valutakurs kan påvirke eksportpriser.

Statistiske mål:

For å forstå datakvaliteten og variasjonen i datasettet, har vi beregnet:
- Gjennomsnitt, for å se den generelle utviklingen i prisnivået.
    ⚪️ Gjennomsnitt er en viktig statistisk måling fordi den representerer den mest typiske verdien og den som ofte er gjentakende i et datasett. Dette kan gi en rask indikasjon der man vet omtrentlig hvor for eksempel prisen kan ligge. Vet man gjennomsnittsprisen kan man tenke at prisen for en dag ligger omtrentlig over eller under gjennomsnittsverdien. Den er sårbar for ekstreme verdier, om det er et unormalt høyt tall for prisen påvirker dette gjennomsnittet og dytter verdien opp.

- Median, som gir et mer robust bilde i tilfelle ekstreme verdier.
    ⚪️ Median viser akkurat midten av et datasett som er sortert fra minst til størst. Median er veldig representativ som et statistisk måleverktøy fordi den viser mer konkret fordeling av dataen i datasettet. Verdien påvirkes ikke like mye av ekstreme verdier slik som gjennomsnitt. Sammenligner man median og gjennomsnitt kan man se etter skjevheter i datasettet og se på om det er store forskjeller. Gjennomsnittet for fersk laksevekt er 13042 og standardavviket er 13550, da tyder dette på at det er minimale skjevheter når disse tallene er veldig like og tyder på at dataene er pålitelige.
    
- Standardavvik, for å måle spredning og volatilitet i prisene.
Vi har analysert denne statistikken både for kr/kg for fersk og frosset laks hvert år, samt prisforskjell per årstid for å se om vi finner en tydelig sesongvariasjon. Disse analysene er viktige å foreta for å lettere kunne forutsi fremtidig kg-pris og antall tonn eksport av laks. 
    ⚪️ Standardavvik viser hvor stor variasjon det er i dataene og er viktig for å se hvor høyt eller lavt en verdi kan bli. I filen "Dataanalyse", ser man at standardavviket generelt for fersk laks kilopris er 23 og dette indikerer et høyt tall sammenlignet med gjennomsnittet fordi lakseprisen kan variere opp og ned med denne verdien for ulike uker. Det samme kan man se for frosset laksevekt, da gjennomsnittet er omtrent 600 og standardavviket er omtrent 300. Dette betyr at i forhold til gjennomsnittet kan vekten svinge opp og ned med halvparten. Som tdiligere nevnt så er det et stort avvik for fersk laksevekt også da den er på omtrent 5700, noe som er mye i forhold til gjennomsnittet. 


Håndtering av datastruktur og skjevheter:

For å sikre pålitelig analyse har vi:
- Renset data for manglende verdier og ufullstendige uker.
- Brukt median sammen med gjennomsnitt for å håndtere skjevheter.
- Aggregert data per uke, per år og per sesong for å se tydeligere mønstre.
- Kontrollert og validert at datastrukturen er jevn (f.eks. kun fredager, enhetlig ukestruktur).

Visualiseringer:

Vi vil videre lage følgende visualiseringer for å støtte analysen:
- Tidsseriegrafer for å vise prisutvikling og valutakurser over tid.
- Dobbel y-akse-plot for å sammenligne valutakurs og kilospris.
- Scatterplot med regresjonslinje for å undersøke styrken på sammenhengen mellom variabler.
- Prisforskjell-plott for å vise utviklingen i gapet mellom fersk og frosset laks.
- Boksplott for å synliggjøre standardavvik og uteliggere i tillegg til median.
Disse visualiseringene gjør det enkelt å identifisere trender og forklare funnene til både tekniske og ikke-tekniske målgrupper.


Når disse statistke verdiene er veldig ulike tyder dette på at det er ustabile data og vanskeligere å predikere for framtidig analyse.
Det er en positiv skjevhet mellom gjennomsnittet og median for kiloprisen av fersk laks. Da medianen er lavere enn gjennomsnittet som betyr at når det er noen uker med veldig høy kilopris trekker gjennomsnittet oppover.


Vi valgte å inkludere både totaloversikt, statistiske mål og visuelle figurer som boksplott og kombinerte grafer for å sikre en grundig og faglig begrunnet analyse. Slik kan man forstå mønstre, avvik, og trender i lakseeksporten på en måte som er forklarende, oversiktlig og forståelig.



Oppgave 5: Visualisering

Spesifikke typer visualiseringer:

I prosjektet er det valgt å bruke linjediagrammer og scatter plots for å vise trender over tid, som endringer i valutakurser (USD/NOK, EUR/NOK) og sammenligning med kilospriser på fersk og frossen laks. Disse visualiseringene gir et klart bilde av hvordan variablene utvikler seg over tid og hvordan de kan være sammenhengende.
For eksempel, ved å bruke linjediagrammer, kan man se den overordnede trenden for priser og valutakurser, mens scatter plots kan hjelpe med å visualisere sammenhengen mellom variabler. Dette kommer klarer frem i oppgave 6.

Bruk av Matplotlib og Seaborn:

Matplotlib har blitt brukt til å lage linjediagrammer som viser utvikling over tid. Det gir god kontroll over aksenes etiketter, farger og legender for å lage klart definerte visualiseringer.
Seaborn er nyttig for å lage scatterplots og korrelasjonsmatriser for å se på sammenhengen mellom variablene. Dette biblioteket gir et enkelt API for visuelle forbedringer, som gjør det lettere å bruke farger og stiler for å formidle informasjon på en effektiv måte.

Håndtering og visualisering av manglende data:

For å håndtere manglende data har vi brukt metoder som fylling av manglende verdier, for eksempel ved bruk av gjennomsnitt, median eller interpolering. Når dataene ikke kan fylles på en pålitelig måte, blir de ekskludert for å unngå forvrengte analyser. Visualiseringer som linjediagrammer og scatterplots gjør det også mulig å merke hvor data mangler (for eksempel ved å bruke spesifikke symboler eller farger), slik at brukerne forstår hvordan analysene håndterer dette.

Interaktive visualiseringer med Plotly:

Plotly er brukt til å lage interaktive linjediagrammer. Plotly gir muligheten til å zoome, bruke hover-effekter og gir brukerne interaktive verktøy som gjør det lettere å utforske dataene. Fordelene med interaktive visualiseringer er at de lar brukerne utforske spesifikke områder av dataene og få mer informasjon om bestemte punkter uten å måtte endre på visualiseringene manuelt.

Evaluering av effektiviteten:

Effektiviteten til visualiseringene har blitt evaluert ved å vurdere hvor lett det er for brukerne å forstå sammenhengene i dataene og hvordan de viktigste funnene presenteres. Interaktive visualiseringer gir bedre tilgjengelighet, ettersom brukerne kan utforske dataene på egen hånd, mens statiske diagrammer gir et mer oversiktlig bilde av de viktigste trendene. Visualiseringene er designet for å være enkle å forstå for både tekniske og ikke-tekniske brukere, og klart merking og intuitiv grafikk hjelper med formidling.



analysen:
Grafen for vekten av eksport og kilopris av fersk laks viser en negativ lineær sammenheng. Dette antyder at et større eksportvolum henger sammen med lavere pris, noe som kan forklares av tilbud og etterspørsel. Prikkene rundt regresjonslinjen viser spredningen i dataene, avvikene, noen uker har større avvik enn andre og dette kan representere sesongvariasjon eller andre hendelser som toll.
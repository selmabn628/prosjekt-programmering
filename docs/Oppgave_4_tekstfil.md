Oppgave 4: Dataanalyse	

I denne delen av prosjektet har vi brukt verktøy som Pandas, NumPy og Matplotlib for å analysere sammenhengen mellom valutakurs og eksportpriser på laks. Formålet har vært å identifisere trender, variasjoner og mønstre i prisutviklingen for fersk og frosset laks over tid, samt undersøke hvordan valutakurs kan påvirke eksportpriser.

Statistiske mål:

For å forstå datakvaliteten og variasjonen i datasettet, har vi beregnet:
- Gjennomsnitt, for å se den generelle utviklingen i prisnivået.
- Median, som gir et mer robust bilde i tilfelle ekstreme verdier.
- Standardavvik, for å måle spredning og volatilitet i prisene.
Vi har analysert denne statistikken både for kr/kg for fersk og frosset laks hvert år, samt prisforskjell per årstid for å se om vi finner en tydelig sesongvariasjon. 

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
Disse visualiseringene gjør det enkelt å identifisere trender og forklare funnene til både tekniske og ikke-tekniske målgrupper.

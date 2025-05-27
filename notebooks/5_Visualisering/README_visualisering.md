Visualisering:

Spesifikke typer visualiseringer:

I prosjektet er det benyttet både linjediagrammer, søylediagrammer og scatter plots for å utforske og formidle sammenhenger mellom variabler. Eksempler inkluderer endringer i valutakurser (USD/NOK og EUR/NOK) over tid, og hvordan disse henger sammen med kilospriser på fersk og frosset laks.
Linjediagrammer er brukt til å vise trender over tid, mens scatterplots tydelig visualiserer styrken i sammenhengene mellom variabler, som valutakurs og eksportpriser. Denne typen visualisering gir innsikt i hvordan valuta og pris påvirker hverandre.

Bruk av Matplotlib og Seaborn:

Matplotlib har blitt brukt til å lage statiske søylediagrammer og linjediagrammer. Dette gir god kontroll over aksenes utseende, etiketter, farger og plassering, og passer godt for figurer i rapporter og presentasjoner. Matplotlib er brukt for å vise en oversiktlig sammenligning av fersk og frosset laks per uke for valgte år (f.eks. 2020).
Seaborn er brukt for å lage scatterplots og regresjonslinjer, blant annet for å visualisere korrelasjonen mellom valutakurser og eksportpriser. Biblioteket gir et ryddig og estetisk uttrykk og er godt egnet for utforskende dataanalyse.

Interaktive visualiseringer med Plotly:

For mer dynamisk utforskning er Plotly brukt til å lage interaktive grafer. Dette inkluderer både linjediagrammer og søylediagrammer med dropdown-meny for å velge år. I søylediagrammene sammenlignes kilospriser på fersk og frosset laks per uke. Brukeren kan velge hvilket år som skal vises via menyen, og figurene oppdateres umiddelbart.

Håndtering og visualisering av manglende data:

Manglende verdier håndteres ved å fjerne ufullstendige observasjoner som ikke kan fylles pålitelig. Dette hindrer at analysene påvirkes negativt. I scatterplots og linjediagrammer vises tydelig hvilke uker som mangler data, og disse er enten utelatt eller markert.

Evaluering av effektiviteten:

Effektiviteten i visualiseringene vurderes ut fra hvor godt de kommuniserer hovedfunn i dataene. Interaktive visualiseringer gir brukeren større frihet til å utforske mønstre og detaljer, mens statiske figurer gir et klart og direkte bilde av utviklingen og brukes der oversikt er viktigst. Kombinasjonen av begge gir en fleksibel og informativ formidling for både tekniske og ikke-tekniske brukere.
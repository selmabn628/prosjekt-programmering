Oppgave 6: Prediktiv analyse

I denne oppgaven bruker vi prediktiv analyse for å forutsi fremtidig eksportverdi av fersk laks basert på historiske priser. Vi benytter lineær regresjon for å identifisere sammenhengen mellom kilopris og eksportverdi, og analyserer hvordan denne modellen kan brukes til å predikere fremtidige inntekter fra lakseeksport.


Visualiseringer og deres formål:

Linjediagrammer:
Vi benyttet linjediagrammer for å vise utviklingen over tid av priser på fersk og frosset laks, samt valutakursene USD/NOK og EUR/NOK. Linjediagrammer er godt egnet til å vise trender over tid og gir en god oversikt over hvordan disse variablene utvikler seg.
For å håndtere manglende data, laget vi en graf som viser hvordan interpolasjon (fylling av manglende verdier) påvirker trendene for fersk og frosset laks. Dette viser tydelig hvilken effekt manglende verdier kan ha på de langsiktige trendene, og hvordan det kan endre analysen av dataene.

Scatterplot:
Et scatterplot ble brukt for å undersøke korrelasjonen mellom valutakursene (USD/NOK, EUR/NOK) og kilosprisen på frosset laks. Scatterplottet hjelper til med å vise hvordan de to variablene henger sammen, og hvilken type forhold (lineært, ikke-lineært) som eksisterer mellom dem. Dette gjør det enklere å visualisere sammenhenger og finne mønstre i dataene.

En positiv korrelasjon på begge valutakursene (EUR/NOK og USD/NOK) med kilosprisen på frosset laks indikerer at valutakursene har en viss påvirkning på prisen på laks. Når en av valutaene styrkes, kan det føre til en økning i prisene på laks, noe som kan skyldes at eksportører trenger mer penger for å kompensere for valutafluktuasjoner eller at høyere valutakurser kan reflektere høyere etterspørsel etter norske produkter som laks.
Det ble funnet en sterk positiv korrelasjon mellom EUR/NOK og kilospris, særlig for fersk laks (r ≈ 0.87). USD/NOK hadde også en positiv, men svakere korrelasjon. Den sterkere korrelasjonen med EUR/NOK kan tyde på at prisen på frosset laks har en større følsomhet for endringer i euroen enn for USD. Dette kan være relatert til at eurosonen er en større handelspartner for Norge når det gjelder sjømat, og derfor har euroen en mer direkte påvirkning på prisene på laks enn USD.

Søylediagram:
Søylediagrammet ble brukt til å sammenligne dataene for fersk og frosset laks i et spesifikt år (2010), noe som gjorde det lettere å se prisforskjellene mellom de to. Søylediagrammer er nyttige for å sammenligne forskjellige grupper (i dette tilfellet, prisene på fersk vs frosset laks) over tid eller på tvers av forskjellige kategorier.
Håndtering av manglende data:

Vi håndterte manglende data på to måter:

Fjerning av manglende verdier (renset data): Vi fjernet observasjoner med manglende verdier for å vise hvordan datatrendene ser ut når vi kun bruker fullstendige data.
Interpolering: Vi fylte de manglende verdiene med interpolering for å se hvordan det påvirker trendene og om det gir et mer realistisk bilde av utviklingen.
Disse teknikkene ble visualisert i flere grafer for å sammenligne hvordan de håndterte manglende data påvirket resultatene.

Evaluering av visualiseringene:

De tre typene visualiseringer – linjediagrammer, scatterplots og søylediagrammer – fungerte godt for å formidle informasjon om prisutviklingen for fersk og frosset laks, samt valutakursene og sammenhengene mellom dem. Linjediagrammet var spesielt nyttig for å visualisere trender over tid, mens scatterplottet ga en god oversikt over korrelasjoner. 
Søylediagrammet var mest effektivt for sammenligning på tvers av grupper for et spesifikt år.

Manglende data ble effektivt håndtert ved å bruke begge metodene, og grafene tydeliggjorde hvordan interpolering kan påvirke den langsiktige trenden, sammenlignet med fjerning av manglende data.

Modellene gir en enkel, men nyttig pekepinn på hvordan prisutvikling kan påvirke eksportinntekter. Likevel er det viktig å være bevisst på at lineær regresjon forutsetter en jevn trend, og ikke fanger opp sesongvariasjoner, politiske endringer eller globale markedsforhold. For en mer presis prediksjon kunne man benyttet mer avanserte modeller som tar høyde for flere variabler.

Grafen som sammenligner eksportverdi, kilopris og vekt viser at det er viktig å analysere både pris og volum, siden eksportverdi er et resultat av begge. Den understreker også at pris ikke nødvendigvis følger volum, noe som er viktig å ta med i en prediktiv modell. I en bærekraftig næring vil det være gunstig å oppnå høy verdi med lavere volum, og denne utviklingen kan tolkes som positiv.
Grafen brukes til å forklare hvordan ulike faktorer påvirker eksportinntektene, og er nyttig for å vurdere både økonomisk og miljømessig effektivitet.

Vi kan tolke fra grafene nederst i filen med prediksjon at når kiloprisen øker fører dette også til at eksportverdien øker. Dette betyr altså at pris har en klar sammenheng der prisen driver eksportverdien oppover. Selv om modellen er ganske forenklet med tanke på at predisksjonen er linær, så gir fortsatt grafene innsikt i hvordan økning i kilopris kan påvirke eksportverdien og derfor brukes som et utgangspunkt til videre planlegging.

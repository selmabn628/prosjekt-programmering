Oppgave 2: Datainnsamling 


Vi har i dette prosjektet identifisert Statistisk sentralbyrås (SSB) API som en relevant, åpen datakilde for analyse av miljødata relatert til norsk lakseoppdrett. Denne datakilden gir innsikt i økonomiske og miljømessige faktorer knyttet til norsk fiskeoppdrett, en næring med betydelig miljøpåvirkning. Vi har valgt tabell 03024 https://www.ssb.no/statbank/table/03024/tableViewLayout1/, som gir detaljert informasjon om eksport av oppalen laks fordelt på varegruppe og tidsperiode. Datasettet inneholder også opplysninger om eksportverdi, eksportvolum og kilospris, noe som gjør det egnet for analyser av økonomiske trender og bærekraft i næringen.

I tillegg har vi supplert med valutakursene USD og EUR fra Norges Bank for å kunne analysere hvordan pris i norske kroner påvirkes av valutamarkedet. https://app.norges-bank.no/query/index.html#/no/currency?currency=USD,EUR&frequency=B&startdate=2000-01-01&stopdate=2025-05-22.

Valget av disse kildene er basert på fire kriterier: kildeautoritet, datakvalitet, tilgjengelighet og brukervennlighet. Både SSB og Norges Bank er offisielle, nasjonale institusjoner for statistikk, noe som sikrer at kildene er pålitelig og at dataene er korrekte. Datasettene er godt dokumentert, oppdateres jevnlig og følger etablerte standarder. Videre er API-ene offentlig tilgjengelig og krever ingen autentisering for å hente ut data. 

For å hente og bearbeide dataene har vi integrert API-et i Python ved hjelp av biblioteket requests, som sender en POST-forespørsel til SSBs server. API-et returnerer data i JSON-stat2-format, som deretter blir konvertert til en Pandas DataFrame for enklere analyse. Denne strukturen gjør det mulig å sortere, filtrere og omstrukturere dataene. Ved å bruke Pandas sikrer vi at dataene struktureres korrekt og kan filtreres for å unngå feil eller uregelmessigheter. Dette gjør det enklere å analysere trender på en pålitelig måte. 

Vi har blant annet omorganisert tabellen for å kunne sammenligne kilospris og eksportvolum for fersk og frossen laks over tid. Dette legger grunnlaget for videre analyser av eksporttrender og variasjoner i priser. 

Datasettet vi har hentet viser tydelige variasjoner i eksportvolum og pris over tid. Foreløpige analyser indikerer at kilosprisen på fersk laks er mer variabel enn på frossen laks, mens eksportvolumet har hatt en stigende trend i enkelte perioder. Foreløpig har vi organisert dataene slik at de er enklere å analysere, og vi har identifisert hvilke faktorer vi ønsker å undersøke videre. Vi har lagt særlig vekt på hvordan kilospris og eksportvolum varierer mellom fersk og frossen laks, og hvordan disse faktorene kan påvirke næringen over tid. Vi vil også estimere CO₂-utslipp fra lakseeksport.  Videre analyse vil kunne gi mer innsikt i sammenhenger mellom markedstrender og produksjonsmengde.

Historgrammet fra visualisere.original.ipynb filen viser at eksportert mengde fersk laks per uke varierer sterkt, men at det er en tendens til høyere volum rundt 5000 tonn og i intervallet 14 000–17 000 tonn. Fordelingen er ikke symmetrisk, og tyder på at enkelte perioder har ekstremt høy eksport, i motsetning ti andre perioder som har mindre eksport.
Dette støttes av den lange halen i høyre del av grafen.

I filen Valutakurs_USD_EUR_api analyserte vi forksjellem mellom valutakursene EUR/NOK og USD/NOK. 
Ved å visualisere differansen mellom disse over tid, fikk vi innsikt i hvordan valutakursene kan påvirke lønnsomheten i ulike eksportmarkeder. En sterkere euro kan bety høyere inntekt for norsk lakseeksport til Europa sammenlignet med USA, gitt at salgsprisen i NOK er den samme. Grafen viser utviklingen av forskjellene og bidrar til å fostå risikoen ved bruk av ulik valuta til bruk i markedsstrategier.
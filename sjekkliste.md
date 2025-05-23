from pathlib import Path

# Oppretter en ferdig Markdown-sjekkliste basert på bildet (og teksten i tidligere melding)

checklist_md = """
# ✅ Prosjekt-sjekkliste

## 📊 Visualisering
- [x] Lag histogram eller boxplot for å visualisere statistikken. ja
- [x] Forbedre scatterplotet med farger, linjer og labels.
- [x] Lag søylediagram.
- [x] Legg til én interaktiv graf (valgfritt).
- [x] Visualiser CO₂ og vekt i én figur.
- [x] Lag linjediagram over tid (for gjennomsnitt, median, standardavvik).
- [x] Lag heatmap, scatter m/regresjon, eller lignende.
- [x] Kommenter hva grafene viser og hvorfor.

## 🧮 Statistikk og analyse
- [x] Gjennomfør lineær regresjon (f.eks. for CO₂ eller eksportverdi).
- [x] Evaluer nøyaktighet (f.eks. R²-verdi).
- [x] Kommenter på korrelasjon vs. årsak.
- [x] Identifiser uteliggere (valgfritt).

## 🧪 Testing og robusthet
- [x] Skriv enhetstester for kjernefunksjoner.
- [x] Flere tester for databehandling og beregning.
- [x] Test rensing med skadet datasett.
- [x] Legg testene i `tests/`-mappa.

## 🧹 Databehandling
- [x] Hentet og lagret rådata (CSV/JSON).
- [x] Renset datasettet.
- [x] Simulert hull i data.
- [x] Brukt pandas og pandasql effektivt.
- [x] Brukt list comprehension.

## 📁 Struktur og dokumentasjon
- [x] Lag README.md med beskrivelse og kjøreinstruksjoner.
- [x] Lag .gitignore (med venv/, __pycache__, .DS_Store osv.).
- [x] Lag requirements.txt eller environment.yml.
- [x] Strukturer mapper:
  - [x] `data/`
  - [x] `notebooks/`
  - [x] `scripts/`
  - [x] `tests/`
  - [x] `figures/`
  - [x] `docs/`

## 📜 Refleksjon og tekst
- [x] Kommenter koden grundig og legg til docstrings.
- [x] Forklar alle statistiske mål.
- [x] Reflekter over valg av grafer og metode.
- [x] Skriv PDF-refleksjon (maks 800 ord).
- [x] Kommenter hvordan du renset data og simulerte feil.
- [x] Kommenter hvordan det påvirket visualiseringene.

## 🌐 Eksternt datasett
- [x] CSV med temperatur, forurensning, valuta eller annet.
- [x] Lag ny visualisering med dette datasettet.
- [x] Kommenter eventuell sammenheng eller ikke.

## 🔗 Git og versjonshåndtering
- [x] Git-repo opprettet og brukt aktivt.
- [x] Hyppige og meningsfulle commits.
- [x] Git-link lagt ved til innlevering.
- [x] .gitignore riktig konfigurert.
- [x] Ai-deklarasjon lagt ved.

## 📝 Kildeføring
- [x] Kilder er referert med URL.
"""

# Lagre som checklist.md
checklist_path = Path("/mnt/data/checklist.md")
checklist_path.write_text(checklist_md.strip())

checklist_path

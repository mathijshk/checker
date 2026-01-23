# AI-Dichtbij Framework Web Applicatie

Een interactieve web applicatie voor het **AI-Dichtbij Framework voor Verantwoord Werken met AI**.

## Over het Framework

Het AI-Dichtbij Framework biedt een praktische aanpak voor maatschappelijke organisaties om verantwoord met AI te werken. Het vermijdt technische en juridische overbelasting, biedt bestuurlijk houvast, en is direct toepasbaar.

### Kernprincipe

> AI verantwoord inzetten betekent: bewust kiezen waar AI helpt, begrenzen waar het schaadt, en organiseren wie verantwoordelijk is.

## Zes Lagen van het Framework

1. **Waarden** - Het morele kompas
2. **Risicologica** - Waar kan het misgaan
3. **Gebruikscategorieën** - Wat mag wel, wat niet
4. **Rollen en Verantwoordelijkheid** - Wie doet wat
5. **Leren en Reflectie** - Een proces, geen vinkje
6. **Minimale Set Documenten** - Voldoende documentatie

## Applicatie Features

### 📖 Framework Verkenning
- Interactieve navigatie door alle 6 lagen
- Gedetailleerde uitleg per laag met praktische voorbeelden
- Reflectievragen voor zelfevaluatie

### ✍️ Interactieve Assessment
- Volledige vragenlijst op basis van alle lagen
- Auto-save functionaliteit (lokaal opslag)
- Geen persoonlijke data verzameling

### 📋 Actieplan Generator
- Automatische analyse van antwoorden
- Gepersonaliseerde aanbevelingen
- Quick wins en lange termijn acties
- Downloadbare resultaten (HTML)

### 🎨 Gebruiksvriendelijk Design
- Modern en toegankelijk interface
- Responsive design voor alle apparaten
- Print-vriendelijke resultaten
- Visuele hulpmiddelen (iconen, kleurcodering)

## Installatie en Gebruik

### Vereisten
```bash
Python 3.8+
Flask 3.0.0
Jinja2 3.1.2
```

### Installatie
```bash
# Installeer dependencies (als ze nog niet geïnstalleerd zijn)
pip install -r requirements.txt
```

### Start de Applicatie
```bash
# Start de AI-Dichtbij app
python3 dichtbij_app.py
```

De applicatie is toegankelijk op: `http://localhost:5001`

### Port Configuratie
De app draait standaard op poort 5001 (om conflicten met de bestaande AI Governance app op poort 5000 te voorkomen).

## Applicatie Structuur

```
dichtbij_app.py                    # Hoofd Flask applicatie
dichtbij_templates/                # HTML templates
  ├── dichtbij_index.html         # Homepage met framework overzicht
  ├── dichtbij_layer.html         # Individuele laag detail pagina
  ├── dichtbij_assessment.html    # Volledige assessment pagina
  └── dichtbij_results.html       # Resultaten en actieplan
dichtbij_static/                   # Statische bestanden
  └── dichtbij_style.css          # Stylesheet
```

## Navigatie Flow

1. **Homepage** (`/`) - Overzicht van het framework
   - Introductie tot de 6 lagen
   - Keuze tussen verkennen of direct assessment

2. **Laag Detail** (`/layer/<layer_id>`) - Diepgaande uitleg per laag
   - Kernprincipes/risico's/zones/etc.
   - Reflectievragen
   - Navigatie naar vorige/volgende laag

3. **Assessment** (`/assessment`) - Volledige vragenlijst
   - Vragen georganiseerd per laag
   - Optionele contactgegevens
   - Auto-save functionaliteit

4. **Resultaten** (`/results`) - Persoonlijk actieplan
   - Overzicht van alle antwoorden
   - Gegenereerd actieplan met:
     - Quick wins (start deze week)
     - Prioriteiten (komende maand)
     - Lange termijn acties
   - Downloadable en printbaar

## API Endpoints

### `GET /`
Homepage met framework overzicht

### `GET /layer/<layer_id>`
Detail pagina voor specifieke laag
- `layer_id`: waarden, risico, gebruik, rollen, leren, documenten

### `GET /assessment`
Volledige assessment pagina met alle reflectievragen

### `POST /api/save-responses`
Opslaan van gebruikersresponsen in sessie
- Body: JSON met responses per laag

### `POST /api/generate-action-plan`
Genereer gepersonaliseerd actieplan op basis van responses
- Body: JSON met responses
- Returns: Actieplan met quick wins, prioriteiten en lange termijn acties

### `GET /results`
Resultaten pagina met actieplan
- Vereist: Opgeslagen responses in sessie

## Gebruikscategorieën (Traffic Light System)

Het framework gebruikt een simpel maar effectief verkeerslicht systeem:

### 🟢 Groene Zone - Laag Risico
Toegestaan zonder extra goedkeuring:
- Teksten herschrijven
- Samenvatten van openbare informatie
- Brainstormen
- Interne notities

### 🟠 Oranje Zone - Verhoogde Aandacht
Alleen met duidelijke afspraken:
- Analyse van dossiers
- Conceptadviezen
- AI-interactie met cliënten of burgers
- Externe publicatie van AI-gegenereerde content

### 🔴 Rode Zone - Niet Toegestaan
Niet toegestaan of alleen na expliciet besluit:
- Geautomatiseerde beslissingen over mensen
- Invoer van vertrouwelijke persoonsgegevens in publieke AI-tools
- AI als vervanger van professioneel oordeel in zorg, onderwijs of toezicht

## Privacy en Data

- **Geen externe opslag**: Alle data blijft lokaal in de browser sessie
- **Auto-save**: Draft antwoorden worden lokaal opgeslagen (localStorage)
- **Optionele contactgegevens**: Email is volledig optioneel
- **Geen tracking**: Geen analytics of tracking cookies

## Waarom dit Framework Werkt

✓ **Vermijdt overbelasting** - Geen technische of juridische complexiteit
✓ **Bestuurlijk houvast** - Duidelijke rollen en verantwoordelijkheden
✓ **AI Act compliant** - Sluit aan zonder juridisch te worden
✓ **Direct toepasbaar** - Praktisch voor maatschappelijke organisaties

## Doelgroep

Deze applicatie is speciaal ontwikkeld voor:
- Maatschappelijke organisaties
- Non-profit sector
- Zorg- en onderwijsinstellingen
- Lokale overheden
- Bestuurders en directeuren
- Beleidsmedewerkers

## Toekomstige Uitbreidingen

Mogelijke verbeteringen:
- [ ] PDF export van actieplan
- [ ] Email functionaliteit voor resultaten
- [ ] Template downloads (AI-principes, gebruikskaders)
- [ ] Voorbeeldcasussen per laag
- [ ] Vergelijking met andere organisaties (geanonimiseerd)
- [ ] Voortgang tracking bij herhaalde assessments

## Licentie

Voor maatschappelijke organisaties

## Contact

Voor vragen of feedback over het framework of de applicatie.

---

**Let op**: Deze applicatie is een hulpmiddel voor reflectie en bewustwording. Het vervangt geen professioneel advies over AI governance en compliance.

# 📅 Agenda Applicatie

Een eenvoudige maar krachtige kalender/agenda applicatie in Python.

## ✨ Functionaliteit

- **📆 Kalender weergave**: Bekijk een maandkalender met markering van dagen met afspraken
- **➕ Afspraken toevoegen**: Maak nieuwe afspraken met titel, datum, tijd, beschrijving en duur
- **📋 Afspraken bekijken**: Overzicht van alle afspraken, gesorteerd op datum
- **📅 Datum filter**: Bekijk alleen afspraken voor een specifieke datum
- **🔍 Zoeken**: Zoek afspraken op basis van titel of beschrijving
- **🗑️ Verwijderen**: Verwijder afspraken die niet meer nodig zijn
- **💾 Automatisch opslaan**: Alle afspraken worden automatisch opgeslagen

## 🚀 Gebruik

### De applicatie starten

```bash
python agenda.py
```

### Navigatie

Het programma heeft een interactief menu:

1. **Bekijk kalender voor een maand** - Toon een maandkalender met gemarkeerde afspraken
2. **Voeg nieuwe afspraak toe** - Maak een nieuwe afspraak aan
3. **Bekijk alle afspraken** - Toon alle afspraken chronologisch
4. **Bekijk afspraken voor een datum** - Filter afspraken op datum
5. **Zoek afspraken** - Zoek in titels en beschrijvingen
6. **Verwijder afspraak** - Verwijder een geselecteerde afspraak
7. **Exit** - Sluit de applicatie af

### Voorbeeld gebruik

#### Kalender bekijken
```
KALENDER BEKIJKEN
================================================
Huidige maand: 1/2026
Wil je de huidige maand bekijken? (j/n): j

==================================================
              Januari 2026
==================================================

  Ma  Di  Wo  Do  Vr  Za  Zo
--------------------------------------------------
        1   2   3   4   5
  6   7   8   9  10  11  12
 13  14  15  16  17  18  19
 20  21  22  23  24  25* 26
 27  28  29  30  31
--------------------------------------------------
* = Afspraak op deze dag
```

#### Afspraak toevoegen
```
NIEUWE AFSPRAAK TOEVOEGEN
================================================

Titel: Vergadering met team
Datum (DD-MM-YYYY): 25-01-2026
Tijd (HH:MM): 14:00
Beschrijving (optioneel): Bespreking Q1 planning
Duur in minuten (standaard 60): 90

✅ Afspraak succesvol toegevoegd!
   25-01-2026 14:00 - Vergadering met team (90 min)
```

## 📁 Projectstructuur

```
calendar/
├── __init__.py              # Package initialisatie
├── event.py                 # Event class definitie
├── calendar_manager.py      # Kalender beheer logica
└── README.md               # Deze documentatie

agenda.py                    # Hoofdapplicatie met UI
calendar_events.json         # Data bestand (automatisch aangemaakt)
```

## 💾 Data opslag

Alle afspraken worden opgeslagen in `calendar_events.json` in JSON formaat. Dit bestand wordt automatisch aangemaakt bij het eerste gebruik.

Voorbeeld formaat:
```json
[
  {
    "title": "Vergadering met team",
    "date": "25-01-2026",
    "time": "14:00",
    "description": "Bespreking Q1 planning",
    "duration": 90
  }
]
```

## 🎯 Features

- ✅ Intuïtieve gebruikersinterface
- ✅ Automatische datum/tijd validatie
- ✅ Persistente data opslag
- ✅ Zoekfunctionaliteit
- ✅ Chronologische sortering
- ✅ Visuele kalenderweergave
- ✅ Nederlandstalige interface

## 🔧 Technische details

- **Python versie**: 3.7+
- **Dependencies**: Alleen standaard Python bibliotheek
- **Data format**: JSON
- **Encoding**: UTF-8

## 📝 Tips

- Gebruik het formaat DD-MM-YYYY voor datums (bijv. 25-01-2026)
- Gebruik het formaat HH:MM voor tijden (bijv. 14:30)
- Dagen met afspraken worden gemarkeerd met een * in de kalenderweergave
- Alle afspraken worden automatisch gesorteerd op datum en tijd
- De zoekfunctie is hoofdletterongevoelig

## 🎓 Voorbeeld workflow

1. **Start de applicatie**: `python agenda.py`
2. **Bekijk de huidige maand**: Kies optie 1
3. **Voeg afspraken toe**: Kies optie 2 en vul de details in
4. **Controleer je planning**: Kies optie 3 voor overzicht
5. **Zoek specifieke afspraken**: Kies optie 5 en voer zoekterm in

---

**Versie:** 1.0.0
**Laatst bijgewerkt:** Januari 2026

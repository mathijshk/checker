# AI Governance Checker

Een interactieve tool om directeuren en bestuurders te helpen met AI-geletterdheid, EU AI Act compliance en governance.

## 🎯 Doel

Deze applicatie helpt bij sessies en opdrachten met directeuren en bestuurders om:
- **AI expliciet te maken** in de organisatie
- **AI-geletterdheid** te verbeteren
- **Compliance met de EU AI Act** te waarborgen
- **Governance rondom AI** te versterken

## ✨ Functionaliteit

### 1. AI Readiness Assessment
- Beoordeel de AI-gereedheid van uw organisatie
- 5 categorieën: Strategie, Data & Infrastructuur, Talent & Skills, Governance & Ethiek, Technologie
- 15 vragen met 1-5 schaal
- Directe aanbevelingen per categorie

### 2. EU AI Act Compliance Checker
- Classificeer AI-systemen volgens risiconiveau
- Verboden, Hoog-risico, Beperkt risico, Minimaal risico
- Controleer compliance aan de hand van specifieke vereisten
- Gedetailleerd compliance rapport

### 3. Governance Framework Analyse
- Beoordeel governance volwassenheid (niveau 1-5)
- 5 principes: Transparantie, Verantwoordelijkheid, Eerlijkheid, Privacy, Veiligheid
- Best practices en aanbevelingen
- Roadmap naar hoger maturity level

### 4. Directierapportage
- Automatisch gegenereerde management samenvatting
- Overzicht van alle assessment resultaten
- Prioritaire actiepunten
- Aanbevolen vervolgstappen

## 🚀 Installatie & Gebruik

### Vereisten
- Python 3.7 of hoger

### Installatie
```bash
git clone <repository-url>
cd checker
```

### De AI Governance Checker Starten
```bash
python main.py
```

### De Agenda Applicatie Starten
```bash
python agenda.py
```

Een eenvoudige kalender/agenda tool om afspraken te beheren. Zie [agenda_lib/README.md](agenda_lib/README.md) voor meer informatie.

### Navigatie
De tool heeft een interactief menu systeem:
1. AI Readiness Assessment - Start met beoordeling van AI-gereedheid
2. AI Act Compliance Checker - Controleer AI-systemen op compliance
3. Governance Framework Analyse - Evalueer governance volwassenheid
4. Genereer Directierapport - Maak een rapport van alle verzamelde data
5. Toon Huidige Sessie Data - Bekijk overzicht van ingevulde assessments
6. Exit - Sluit de applicatie af

## 📊 Workflow voor Directiesessies

### Aanbevolen volgorde:

1. **Voorbereiding**
   - Lees `templates/sessie_voorbereiding.md`
   - Verzamel relevante informatie over AI-initiatieven
   - Identificeer deelnemers (CIO, juridisch, compliance, etc.)

2. **Tijdens de sessie**
   - Start met AI Readiness Assessment (45 min)
   - Voer AI Act Compliance Check uit voor belangrijkste systemen (30 min)
   - Beoordeel Governance Framework (30 min)
   - Bespreek resultaten en genereer rapport (15 min)

3. **Na de sessie**
   - Deel het gegenereerde rapport met stakeholders
   - Plan vervolgacties op basis van aanbevelingen
   - Schedule follow-up sessie (3-6 maanden)

## 📁 Projectstructuur

```
checker/
├── main.py                          # AI Governance Checker hoofdapplicatie
├── agenda.py                        # Agenda/Kalender applicatie
├── src/
│   ├── assessment/
│   │   └── readiness.py            # AI readiness assessment module
│   ├── compliance/
│   │   └── ai_act_checker.py       # AI Act compliance checker
│   ├── governance/
│   │   └── framework.py            # Governance framework module
│   └── reports/
│       └── generator.py            # Rapport generatie module
├── agenda_lib/                      # Agenda applicatie module
│   ├── event.py                     # Event class
│   ├── calendar_manager.py         # Kalender beheer
│   └── README.md                   # Agenda documentatie
├── templates/
│   └── sessie_voorbereiding.md     # Sessie voorbereiding template
├── tests/
│   └── test_report_generator.py    # Unit tests
├── reports/                         # Gegenereerde rapporten (auto-created)
└── README.md
```

## 📝 Voorbeeld Output

### AI Readiness Scores
```
Strategie........................ 3.7/5.0  [███░░]
Data & Infrastructuur............ 4.0/5.0  [████░]
Talent & Skills.................. 2.3/5.0  [██░░░]
Governance & Ethiek.............. 3.0/5.0  [███░░]
Technologie...................... 3.5/5.0  [███░░]

TOTAAL GEMIDDELDE: 3.3/5.0
```

### AI Act Compliance
```
Systeem: HR Recruitment AI
Risico Niveau: HIGH (Hoog-risico systemen)
Compliance: 70% (7/10 vereisten voldaan)
Status: ✗ Niet volledig compliant
```

### Governance Maturity
```
OVERALL MATURITY LEVEL: 3/5
Gedefinieerd - Gedocumenteerde standaarden
```

## 🎓 Tips voor Facilitators

- **Wees objectief**: Eerlijke scores zijn belangrijker dan hoge scores
- **Stimuleer discussie**: Verschillende perspectieven leiden tot beter inzicht
- **Maak het concreet**: Gebruik praktijkvoorbeelden uit de organisatie
- **Focus op actie**: Zorg dat elke sessie eindigt met concrete vervolgstappen

## 🔍 Volgende Ontwikkelingen

Mogelijke uitbreidingen:
- Export naar PDF formaat
- Historische trend analyse
- Benchmark met andere organisaties
- AI risk register functionaliteit
- Integration met project management tools

## 📄 Licentie

Deze tool is ontwikkeld om organisaties te helpen met verantwoorde AI implementatie.

## 🤝 Contact & Support

Voor vragen of ondersteuning bij het gebruiken van deze tool, neem contact op met de ontwikkelaar.

---

**Versie:** 1.0.0
**Laatst bijgewerkt:** Januari 2026

# Quick Start Guide - AI Governance Assessment Web App

## Wat je hebt gekregen

Een volledig functionele Nederlandse AI Governance Assessment tool voor je website met:

✅ **16 strategische vragen** voor directeuren en bestuurders
✅ **4 key domeinen**: Oversight, Compliance, Operations, Culture (+ Data Governance & Strategy)
✅ **4 maturity levels**: Foundational, Responsive, Proactive, Leader
✅ **Automatische email** met gepersonaliseerde resultaten
✅ **Responsive design** - werkt op alle devices
✅ **Professionele styling** geïnspireerd op SAS assessment

## Snelstart (3 stappen)

### Stap 1: Installeer Dependencies

```bash
pip install -r requirements.txt
```

Dit installeert:
- Flask (web framework)
- Flask-Mail (email functionaliteit)
- ReportLab (PDF generatie, optioneel)
- Markdown (voor email formatting)

### Stap 2: Configureer Email

```bash
# Kopieer example file
cp .env.example .env

# Bewerk .env met je favoriete editor
nano .env
```

Vul in (voorbeeld voor Gmail):
```env
SECRET_KEY=willekeurige-lange-string-hier
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=jouw-email@gmail.com
MAIL_PASSWORD=jouw-gmail-app-wachtwoord
MAIL_DEFAULT_SENDER=noreply@jouwebsite.nl
```

**BELANGRIJK voor Gmail:**
- Gebruik geen gewoon wachtwoord!
- Maak een App Password aan: https://support.google.com/accounts/answer/185833
- Je moet 2-factor authenticatie enabled hebben

### Stap 3: Start de App

```bash
python app.py
```

Open je browser: **http://localhost:5000**

## Testing

Verifieer dat alles werkt:

```bash
python test_webapp.py
```

Dit checkt:
- ✓ Alle dependencies geïnstalleerd
- ✓ Alle templates aanwezig
- ✓ Alle routes functioneel
- ✓ Assessment vragen correct geconfigureerd

## De Assessment Gebruiken

1. **Landing Page** (`/`)
   - Introductie van de AI Governance Map
   - Uitleg van maturity levels
   - Call-to-action om te starten

2. **Assessment** (`/assessment`)
   - 16 vragen met 5-punt schaal
   - Progress indicator
   - Email capture aan het einde
   - Privacy consent checkbox

3. **Resultaten** (`/results`)
   - Overall maturity score
   - Scores per domein
   - Gepersonaliseerde aanbevelingen
   - Volgende stappen
   - Print functionaliteit

4. **Email**
   - Automatisch verstuurd naar ingevuld adres
   - Bevat alle resultaten + aanbevelingen
   - Professioneel HTML design

## De 16 Assessment Vragen

### Oversight (3 vragen)
1. Senior management betrokkenheid bij AI governance
2. Gedefinieerde AI governance structuur
3. Monitoring van AI-gerelateerde risico's

### Compliance (3 vragen)
4. Grenzen en richtlijnen voor AI-gebruik
5. AI compliance assessments
6. Voorbereiding op AI wetgeving (EU AI Act)

### Operations (4 vragen)
7. Infrastructuur voor verantwoorde AI
8. AI model lifecycle management
9. Balans tussen waarde en risico
10. Transparantie van AI systemen

### Culture (3 vragen)
11. Bewustzijn van AI governance en ethiek
12. Training voor verantwoord AI werken
13. Integratie van governance in dagelijkse processen

### Data Governance (2 vragen)
14. Data quality en bias management
15. Privacy en data protection

### Strategy (1 vraag)
16. AI strategie en roadmap

## Customization

### Vragen Aanpassen

Bewerk `app.py`, zoek naar `ASSESSMENT_QUESTIONS`:

```python
ASSESSMENT_QUESTIONS = [
    {
        'id': 1,
        'category': 'Oversight',
        'question': 'Jouw eigen vraag hier?',
        'options': [
            {'value': 1, 'label': 'Optie 1'},
            {'value': 2, 'label': 'Optie 2'},
            # ... tot 5
        ]
    },
    # Voeg meer vragen toe...
]
```

### Kleuren/Branding Aanpassen

Bewerk `static/style.css`:

```css
:root {
    --primary-color: #0066cc;    /* Jouw hoofdkleur */
    --secondary-color: #00a8ff;  /* Jouw accent kleur */
}
```

### Logo Toevoegen

Bewerk alle templates, vervang:
```html
<h1>AI Governance Assessment</h1>
```

Met:
```html
<img src="{{ url_for('static', filename='logo.png') }}" alt="Logo">
```

## Deployment

### Optie 1: Heroku (gratis tier)

```bash
# Installeer Heroku CLI, dan:
heroku login
heroku create jouw-app-naam
heroku config:set MAIL_SERVER=smtp.gmail.com
heroku config:set MAIL_USERNAME=jouw-email@gmail.com
heroku config:set MAIL_PASSWORD=jouw-app-password
heroku config:set MAIL_DEFAULT_SENDER=noreply@jouwsite.nl
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")

# Voeg Procfile toe
echo "web: gunicorn app:app" > Procfile

# Deploy
git add .
git commit -m "Deploy AI Governance Assessment"
git push heroku main
```

### Optie 2: VPS (DigitalOcean, Linode, etc.)

1. Upload files naar server
2. Install Python 3.9+
3. Install dependencies: `pip install -r requirements.txt gunicorn`
4. Configure Nginx reverse proxy
5. Run with: `gunicorn -w 4 -b 127.0.0.1:5000 app:app`
6. Use systemd for auto-restart

### Optie 3: Docker

```bash
# Dockerfile is included
docker build -t ai-assessment .
docker run -p 5000:5000 --env-file .env ai-assessment
```

## Troubleshooting

### "Connection refused" bij email

**Probleem:** Email wordt niet verzonden

**Oplossing:**
- Check `.env` configuratie
- Voor Gmail: gebruik App Password
- Test: `telnet smtp.gmail.com 587`

### Vragen worden niet getoond

**Probleem:** Lege assessment pagina

**Oplossing:**
- Check browser console (F12)
- Verify `ASSESSMENT_QUESTIONS` syntax in app.py
- Check Flask logs

### Styling werkt niet

**Probleem:** Geen CSS

**Oplossing:**
- Hard refresh (Ctrl+F5)
- Check `static/style.css` exists
- Browser DevTools Network tab

## Files Overzicht

```
checker/
├── app.py                          # ⭐ Main Flask application
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment template
├── test_webapp.py                  # Test suite
├── WEB_README.md                   # Uitgebreide documentatie
├── QUICK_START.md                  # Dit bestand
├── templates/
│   ├── index.html                 # Landing page
│   ├── assessment.html            # Assessment vragen
│   ├── results.html               # Resultaten display
│   └── email_results.html         # Email template
├── static/
│   └── style.css                  # Styling
└── src/                           # Bestaande CLI modules (niet nodig voor web)
```

## Volgende Stappen

1. **Test lokaal** - Verifieer dat alles werkt op localhost
2. **Customize** - Pas kleuren, logo en teksten aan naar jouw merk
3. **Configure email** - Test dat emails echt aankomen
4. **Deploy** - Zet online op je hosting platform
5. **Share** - Deel de link met je doelgroep!

## Support Opties

Als je hulp nodig hebt:

1. **Technische issues**: Check `WEB_README.md` voor gedetailleerde troubleshooting
2. **Vragen aanpassen**: Alle vragen staan in `app.py` (regel ~30-300)
3. **Design aanpassingen**: Alle styling in `static/style.css`

## Extra Features (optioneel)

Later toevoegen:
- PDF export van resultaten
- Database opslag voor analytics
- Admin dashboard voor alle resultaten
- Vergelijking met industry benchmarks
- Multi-language support
- API voor integraties

## Privacy & GDPR

De huidige implementatie:
- ✓ Vraagt expliciet consent
- ✓ Legt privacy statement uit
- ✓ Slaat alleen scores op (in session, tijdelijk)
- ✓ Email alleen gebruikt voor resultaten

Voor volledige GDPR compliance:
- Voeg privacy policy pagina toe
- Implementeer data verwijdering op verzoek
- Log email adressen met timestamp
- Implementeer retention policy

---

**Succes met je AI Governance Assessment! 🚀**

Vragen? Lees `WEB_README.md` voor complete documentatie.

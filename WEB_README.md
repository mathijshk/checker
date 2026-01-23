# AI Governance Assessment - Web Applicatie

Een Nederlandse web-based assessment tool voor directeuren en bestuurders om hun AI governance maturity te meten.

## Overzicht

Deze tool helpt organisaties om:
- Hun huidige AI governance positie te bepalen
- Te benchmarken tegen industry standards
- Gepersonaliseerde aanbevelingen te ontvangen
- Een actieplan te ontwikkelen voor verbetering

## Features

✅ **16 Strategische Vragen** - Gebaseerd op de AI Governance Map
✅ **4 Key Domeinen** - Oversight, Compliance, Operations, Culture
✅ **4 Maturity Levels** - Foundational, Responsive, Proactive, Leader
✅ **Email Resultaten** - Automatische versturen van persoonlijke resultaten
✅ **Responsive Design** - Werkt op desktop, tablet en mobiel
✅ **Privacy-First** - Anonieme data collectie

## Installatie

### 1. Installeer Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configureer Email Settings

Kopieer het voorbeeld environment bestand:

```bash
cp .env.example .env
```

Bewerk `.env` en vul je email configuratie in:

**Voor Gmail:**
```env
SECRET_KEY=genereer-een-random-key
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=jouw-email@gmail.com
MAIL_PASSWORD=jouw-app-wachtwoord
MAIL_DEFAULT_SENDER=noreply@jouwebsite.nl
```

**Belangrijke notities voor Gmail:**
- Gebruik een [App Password](https://support.google.com/accounts/answer/185833), niet je reguliere wachtwoord
- Schakel 2-factor authenticatie in op je Google account
- Genereer een app-specifiek wachtwoord via je Google account settings

**Voor SendGrid:**
```env
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USERNAME=apikey
MAIL_PASSWORD=jouw-sendgrid-api-key
MAIL_DEFAULT_SENDER=noreply@jouwebsite.nl
```

### 3. Start de Applicatie

**Development mode:**
```bash
python app.py
```

De applicatie draait nu op: `http://localhost:5000`

**Production mode (met Gunicorn):**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Gebruik

### Voor Eindgebruikers

1. **Start Assessment** - Open `http://localhost:5000` in je browser
2. **Beantwoord Vragen** - 16 vragen over 4 governance domeinen (10-15 minuten)
3. **Vul Email In** - Ontvang resultaten direct per email
4. **Bekijk Resultaten** - Direct online + gedetailleerd per email

### Voor Ontwikkelaars

#### Projectstructuur

```
checker/
├── app.py                      # Flask web applicatie
├── requirements.txt            # Python dependencies
├── .env                        # Environment variabelen (niet in git!)
├── templates/                  # HTML templates
│   ├── index.html             # Landing page
│   ├── assessment.html        # Assessment vragen
│   ├── results.html           # Results display
│   └── email_results.html     # Email template
├── static/
│   └── style.css              # Styling
└── src/                       # Bestaande Python modules
    ├── assessment/
    ├── compliance/
    ├── governance/
    └── reports/
```

#### API Endpoints

**GET /** - Landing page
**GET /assessment** - Assessment pagina
**POST /submit** - Verwerk assessment (JSON)
**GET /results** - Toon resultaten

#### Assessment Vragen Aanpassen

Bewerk `ASSESSMENT_QUESTIONS` in `app.py`:

```python
ASSESSMENT_QUESTIONS = [
    {
        'id': 1,
        'category': 'Oversight',
        'question': 'Jouw vraag hier?',
        'options': [
            {'value': 1, 'label': 'Laagste niveau'},
            {'value': 5, 'label': 'Hoogste niveau'}
        ]
    },
    # ... meer vragen
]
```

#### Scoring Logic Aanpassen

Zie functies in `app.py`:
- `calculate_results()` - Bereken scores per categorie
- `get_maturity_level()` - Bepaal maturity level
- `get_recommendations()` - Genereer aanbevelingen
- `get_category_advice()` - Specifiek advies per categorie

## Deployment

### Option 1: Traditionele Hosting

Upload naar je webserver en configureer:
- Python 3.7+
- Reverse proxy (Nginx/Apache) naar Flask app
- SSL certificaat voor HTTPS
- Environment variables configureren

### Option 2: Cloud Platforms

**Heroku:**
```bash
# Voeg toe: Procfile
web: gunicorn app:app

# Deploy
heroku create jouw-app-naam
heroku config:set MAIL_SERVER=smtp.gmail.com
heroku config:set MAIL_USERNAME=jouw-email@gmail.com
# ... andere env vars
git push heroku main
```

**DigitalOcean App Platform:**
- Connect GitHub repository
- Configureer environment variables in UI
- Auto-deploy on push

**AWS Elastic Beanstalk:**
```bash
eb init -p python-3.9 ai-governance-assessment
eb create production
eb setenv MAIL_SERVER=smtp.gmail.com MAIL_USERNAME=...
eb deploy
```

### Option 3: Docker

```dockerfile
# Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

```bash
docker build -t ai-governance-assessment .
docker run -p 5000:5000 --env-file .env ai-governance-assessment
```

## Security Checklist

- [ ] Gebruik sterke `SECRET_KEY` (min 32 random characters)
- [ ] Gebruik App Passwords voor email, niet je reguliere password
- [ ] Voeg `.env` toe aan `.gitignore`
- [ ] Gebruik HTTPS in productie
- [ ] Enable CORS only voor je eigen domain
- [ ] Rate limiting implementeren (flask-limiter)
- [ ] Input validation op alle formulieren
- [ ] Regelmatig dependencies updaten

## Customization

### Branding

**Logo/Header aanpassen:**
Bewerk `templates/index.html` en andere templates, vervang `<h1>AI Governance Assessment</h1>` met je logo.

**Kleuren aanpassen:**
Bewerk CSS variabelen in `static/style.css`:
```css
:root {
    --primary-color: #jouwkleur;
    --secondary-color: #jouwkleur;
}
```

### Content

**Intro tekst:** Bewerk `templates/index.html`
**Vragen:** Bewerk `ASSESSMENT_QUESTIONS` in `app.py`
**Email template:** Bewerk `templates/email_results.html`
**Aanbevelingen logic:** Bewerk `get_category_advice()` in `app.py`

## Troubleshooting

### Email wordt niet verzonden

**Fout:** "Connection refused" of "Authentication failed"

**Oplossingen:**
1. Check of `MAIL_USERNAME` en `MAIL_PASSWORD` correct zijn
2. Voor Gmail: gebruik App Password, niet regulier password
3. Check firewall settings (port 587 moet open zijn)
4. Test email settings met:
```python
python -c "from app import mail, app; app.app_context().push(); print('Mail configured')"
```

### Styling werkt niet

**Fout:** CSS wordt niet geladen

**Oplossingen:**
1. Check of `static/style.css` bestaat
2. Hard refresh browser (Ctrl+F5)
3. Check browser console voor errors

### Assessment vragen worden niet getoond

**Fout:** Lege pagina op /assessment

**Oplossingen:**
1. Check Flask logs voor errors
2. Verify `ASSESSMENT_QUESTIONS` syntax in app.py
3. Check browser console voor JavaScript errors

## Performance Optimizatie

Voor high-traffic scenarios:

1. **Caching:**
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

2. **Async Email:**
```python
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# In send_results_email():
Thread(target=send_async_email, args=(app._get_current_object(), msg)).start()
```

3. **Database voor resultaten:**
Overweeg SQLite of PostgreSQL voor persistente opslag

## Support

Voor vragen of problemen:
- Check de [CLI README](README.md) voor achtergrond info
- Review test resultaten in [TEST_RESULTATEN.md](TEST_RESULTATEN.md)

## License

© 2026 AI Governance Assessment

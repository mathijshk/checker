"""
AI Governance Assessment - Web Application
Nederlandse versie voor directeuren en bestuurders
"""

from flask import Flask, render_template, request, jsonify, session, redirect
from flask_mail import Mail, Message
import os
from datetime import datetime
import secrets
from src.assessment.readiness import AIReadinessAssessment
from src.reports.generator import ReportGenerator

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(16))

# Email configuratie
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@aigovernance.nl')

mail = Mail(app)

# Assessment vragen - gebaseerd op AI Governance Map
ASSESSMENT_QUESTIONS = [
    {
        'id': 1,
        'category': 'Oversight',
        'question': 'Hoe betrokken is het senior management bij AI governance?',
        'options': [
            {'value': 1, 'label': 'Weinig tot geen betrokkenheid of bewustzijn'},
            {'value': 2, 'label': 'Incidentele betrokkenheid; basisbeginselen aanwezig maar inconsistent toezicht'},
            {'value': 3, 'label': 'Toegewezen rollen en middelen; regelmatig toezicht en rapportage'},
            {'value': 4, 'label': 'Actieve governance met duidelijke verantwoordelijkheid en prestatie-tracking'},
            {'value': 5, 'label': 'Publieke championing van verantwoorde AI; externe betrokkenheid en leiderschap'}
        ]
    },
    {
        'id': 2,
        'category': 'Oversight',
        'question': 'Heeft uw organisatie een gedefinieerde AI governance structuur?',
        'options': [
            {'value': 1, 'label': 'Geen formele structuur of verantwoordelijkheden'},
            {'value': 2, 'label': 'Informele structuur, ad-hoc besluitvorming'},
            {'value': 3, 'label': 'Gedefinieerde AI board of committee met duidelijke mandaat'},
            {'value': 4, 'label': 'Cross-functionele governance met regelmatige reviews en escalatieprocedures'},
            {'value': 5, 'label': 'Volledig geïntegreerde governance die extern gerapporteerd wordt'}
        ]
    },
    {
        'id': 3,
        'category': 'Oversight',
        'question': 'Hoe monitort u AI-gerelateerde risico\'s en incidenten?',
        'options': [
            {'value': 1, 'label': 'Geen systematische monitoring'},
            {'value': 2, 'label': 'Reactieve monitoring; incidenten worden ad-hoc behandeld'},
            {'value': 3, 'label': 'Proactieve risico-identificatie met gedefinieerde escalatiepaden'},
            {'value': 4, 'label': 'Real-time monitoring met KPI\'s en periodieke risk assessments'},
            {'value': 5, 'label': 'Voorspellende risico-analytics met publieke transparantie'}
        ]
    },
    {
        'id': 4,
        'category': 'Compliance',
        'question': 'Zijn er duidelijke grenzen en richtlijnen voor AI-gebruik in uw organisatie?',
        'options': [
            {'value': 1, 'label': 'Geen gedefinieerde grenzen of beleid'},
            {'value': 2, 'label': 'Informele richtlijnen, niet consistent toegepast'},
            {'value': 3, 'label': 'Gedocumenteerd AI-beleid met duidelijke acceptable use boundaries'},
            {'value': 4, 'label': 'Beleid geïntegreerd in workflows met compliance monitoring'},
            {'value': 5, 'label': 'Industrie-leidende standaarden met externe certificering'}
        ]
    },
    {
        'id': 5,
        'category': 'Compliance',
        'question': 'Hoe gaat uw organisatie om met AI compliance assessments?',
        'options': [
            {'value': 1, 'label': 'Geen compliance assessments uitgevoerd'},
            {'value': 2, 'label': 'Incidentele checks voor specifieke projecten'},
            {'value': 3, 'label': 'Regelmatige compliance audits met gedocumenteerde processen'},
            {'value': 4, 'label': 'Geautomatiseerde compliance checks met continuous monitoring'},
            {'value': 5, 'label': 'Third-party validated compliance met publieke rapportage'}
        ]
    },
    {
        'id': 6,
        'category': 'Compliance',
        'question': 'Hoe bereidt uw organisatie zich voor op AI wetgeving zoals de EU AI Act?',
        'options': [
            {'value': 1, 'label': 'Geen bewustzijn of voorbereiding'},
            {'value': 2, 'label': 'Basiskennis aanwezig, nog geen actieve voorbereiding'},
            {'value': 3, 'label': 'Gap-analyse uitgevoerd met remediation roadmap'},
            {'value': 4, 'label': 'Actieve implementatie van compliance requirements'},
            {'value': 5, 'label': 'Volledig compliant en bijdragend aan industrie-standaarden'}
        ]
    },
    {
        'id': 7,
        'category': 'Operations',
        'question': 'Heeft uw organisatie de juiste infrastructuur voor verantwoorde AI?',
        'options': [
            {'value': 1, 'label': 'Geen specifieke AI infrastructuur'},
            {'value': 2, 'label': 'Basis infrastructuur zonder governance controls'},
            {'value': 3, 'label': 'Gedefinieerde AI platforms met logging en monitoring'},
            {'value': 4, 'label': 'Enterprise AI platform met volledige governance integratie'},
            {'value': 5, 'label': 'Best-in-class infrastructuur met industry contributions'}
        ]
    },
    {
        'id': 8,
        'category': 'Operations',
        'question': 'Hoe beheert u AI modellen gedurende hun levenscyclus?',
        'options': [
            {'value': 1, 'label': 'Geen formeel model management'},
            {'value': 2, 'label': 'Basis versioning, ad-hoc updates'},
            {'value': 3, 'label': 'Model registry met versioning en approval workflows'},
            {'value': 4, 'label': 'MLOps met automated testing, monitoring en retraining'},
            {'value': 5, 'label': 'Volledig geïntegreerde ML lifecycle met continuous governance'}
        ]
    },
    {
        'id': 9,
        'category': 'Operations',
        'question': 'Hoe maximaliseert u de waarde van AI terwijl u risico\'s beheerst?',
        'options': [
            {'value': 1, 'label': 'Geen gestructureerde aanpak voor value vs risk balancing'},
            {'value': 2, 'label': 'Informele afwegingen per project'},
            {'value': 3, 'label': 'Gedefinieerde risk-benefit framework voor AI projecten'},
            {'value': 4, 'label': 'Kwantitatieve risk-value assessments met portfolio management'},
            {'value': 5, 'label': 'Data-driven optimization van AI portfolio met externe benchmarking'}
        ]
    },
    {
        'id': 10,
        'category': 'Operations',
        'question': 'Hoe transparant zijn uw AI systemen naar gebruikers en stakeholders?',
        'options': [
            {'value': 1, 'label': 'Geen transparantie over AI gebruik'},
            {'value': 2, 'label': 'Minimale disclosure bij direct gebruik'},
            {'value': 3, 'label': 'Duidelijke AI disclosure met basis uitleg van impact'},
            {'value': 4, 'label': 'Uitgebreide transparantie met explainability features'},
            {'value': 5, 'label': 'Volledige transparantie met publieke AI registers en impact assessments'}
        ]
    },
    {
        'id': 11,
        'category': 'Culture',
        'question': 'Hoe bewust zijn medewerkers van AI governance en ethiek?',
        'options': [
            {'value': 1, 'label': 'Minimaal bewustzijn in de organisatie'},
            {'value': 2, 'label': 'Basis awareness bij direct betrokkenen'},
            {'value': 3, 'label': 'Reguliere training en communicatie over AI governance'},
            {'value': 4, 'label': 'AI ethics is onderdeel van onboarding en performance management'},
            {'value': 5, 'label': 'Cultuur van responsible AI met externe thought leadership'}
        ]
    },
    {
        'id': 12,
        'category': 'Culture',
        'question': 'Hoe zijn teams opgeleid om verantwoord met AI te werken?',
        'options': [
            {'value': 1, 'label': 'Geen specifieke AI training'},
            {'value': 2, 'label': 'Ad-hoc training voor specifieke tools'},
            {'value': 3, 'label': 'Gestructureerd AI training programma voor relevante rollen'},
            {'value': 4, 'label': 'Comprehensive upskilling met certifications en continuous learning'},
            {'value': 5, 'label': 'Center of excellence met internal en external knowledge sharing'}
        ]
    },
    {
        'id': 13,
        'category': 'Culture',
        'question': 'Hoe is AI governance verweven in dagelijkse werkprocessen?',
        'options': [
            {'value': 1, 'label': 'AI governance is geen onderdeel van dagelijkse praktijk'},
            {'value': 2, 'label': 'Governance wordt reactief toegepast bij issues'},
            {'value': 3, 'label': 'Governance checkpoints zijn geïntegreerd in development lifecycle'},
            {'value': 4, 'label': 'Governance is embedded in alle AI-related processen'},
            {'value': 5, 'label': 'Governance is organisatie-brede mindset met continuous improvement'}
        ]
    },
    {
        'id': 14,
        'category': 'Data Governance',
        'question': 'Hoe beheert uw organisatie data quality en bias in AI systemen?',
        'options': [
            {'value': 1, 'label': 'Geen systematische aanpak voor data quality of bias detection'},
            {'value': 2, 'label': 'Ad-hoc checks tijdens development'},
            {'value': 3, 'label': 'Gedefinieerde data quality standards en bias testing protocols'},
            {'value': 4, 'label': 'Automated data quality monitoring en bias detection in productie'},
            {'value': 5, 'label': 'Continuous data quality optimization met fairness metrics en public reporting'}
        ]
    },
    {
        'id': 15,
        'category': 'Data Governance',
        'question': 'Hoe waarborgt u privacy en data protection in AI applicaties?',
        'options': [
            {'value': 1, 'label': 'Geen specifieke privacy maatregelen voor AI'},
            {'value': 2, 'label': 'Basis compliance met algemene privacy policies'},
            {'value': 3, 'label': 'AI-specifieke privacy controls (privacy by design, data minimization)'},
            {'value': 4, 'label': 'Privacy-enhancing technologies (PETs) en regelmatige privacy audits'},
            {'value': 5, 'label': 'Leading edge privacy practices met zero-knowledge AI en differential privacy'}
        ]
    },
    {
        'id': 16,
        'category': 'Strategy',
        'question': 'Heeft uw organisatie een duidelijke AI strategie en roadmap?',
        'options': [
            {'value': 1, 'label': 'Geen gedefinieerde AI strategie'},
            {'value': 2, 'label': 'Experimentele AI projecten zonder overkoepelende strategie'},
            {'value': 3, 'label': 'Gedocumenteerde AI strategie met business alignment'},
            {'value': 4, 'label': 'AI strategie geïntegreerd in corporate strategy met clear ROI targets'},
            {'value': 5, 'label': 'AI als core differentiator met market-leading innovation'}
        ]
    }
]

def calculate_results(answers):
    """Bereken assessment resultaten op basis van antwoorden."""

    # Groepeer scores per categorie
    category_scores = {}
    for question in ASSESSMENT_QUESTIONS:
        cat = question['category']
        if cat not in category_scores:
            category_scores[cat] = []

        answer = answers.get(str(question['id']))
        if answer:
            category_scores[cat].append(int(answer))

    # Bereken gemiddelde per categorie
    results = {}
    total_score = 0
    total_questions = 0

    for category, scores in category_scores.items():
        if scores:
            avg = sum(scores) / len(scores)
            results[category] = {
                'score': round(avg, 1),
                'percentage': round((avg / 5) * 100, 1),
                'level': get_maturity_level(avg)
            }
            total_score += sum(scores)
            total_questions += len(scores)

    # Bereken overall score
    overall_score = round(total_score / total_questions, 1) if total_questions > 0 else 0
    overall_percentage = round((overall_score / 5) * 100, 1)

    return {
        'categories': results,
        'overall': {
            'score': overall_score,
            'percentage': overall_percentage,
            'level': get_maturity_level(overall_score)
        },
        'timestamp': datetime.now().isoformat()
    }

def get_maturity_level(score):
    """Bepaal maturity level op basis van score."""
    if score < 2:
        return 'Foundational'
    elif score < 3:
        return 'Responsive'
    elif score < 4:
        return 'Proactive'
    else:
        return 'Leader'

def get_recommendations(results):
    """Genereer aanbevelingen op basis van resultaten."""
    recommendations = []

    for category, data in results['categories'].items():
        score = data['score']
        level = data['level']

        if score < 3:
            recommendations.append({
                'priority': 'Hoog',
                'category': category,
                'advice': get_category_advice(category, level)
            })
        elif score < 4:
            recommendations.append({
                'priority': 'Gemiddeld',
                'category': category,
                'advice': get_category_advice(category, level)
            })

    return recommendations

def get_category_advice(category, level):
    """Geef specifiek advies per categorie en niveau."""
    advice_map = {
        'Oversight': {
            'Foundational': 'Creëer een AI governance board met duidelijke verantwoordelijkheden en betrek senior management.',
            'Responsive': 'Formaliseer governance processen en implementeer regelmatige risk reviews.',
            'Proactive': 'Implementeer data-driven governance met KPI tracking en external benchmarking.'
        },
        'Compliance': {
            'Foundational': 'Start met het documenteren van AI use cases en voer een EU AI Act gap analyse uit.',
            'Responsive': 'Implementeer compliance checkpoints in de AI development lifecycle.',
            'Proactive': 'Automatiseer compliance monitoring en streef naar third-party certificering.'
        },
        'Operations': {
            'Foundational': 'Implementeer basis AI infrastructure met logging en monitoring capabilities.',
            'Responsive': 'Ontwikkel MLOps practices voor model lifecycle management.',
            'Proactive': 'Optimaliseer AI portfolio met geavanceerde monitoring en continuous improvement.'
        },
        'Culture': {
            'Foundational': 'Start AI awareness programma\'s en basis training voor alle medewerkers.',
            'Responsive': 'Integreer AI ethics in performance management en onboarding.',
            'Proactive': 'Bouw een center of excellence en stimuleer externe thought leadership.'
        },
        'Data Governance': {
            'Foundational': 'Implementeer data quality standards en begin met bias testing.',
            'Responsive': 'Automatiseer data quality monitoring en privacy controls.',
            'Proactive': 'Implementeer privacy-enhancing technologies en publieke fairness metrics.'
        },
        'Strategy': {
            'Foundational': 'Ontwikkel een AI strategie die aligned is met business doelen.',
            'Responsive': 'Integreer AI strategie in corporate strategy met duidelijke ROI targets.',
            'Proactive': 'Position AI als core differentiator met market-leading innovation.'
        }
    }

    return advice_map.get(category, {}).get(level, 'Continue met verbeteren van best practices.')

def send_results_email(email, results, recommendations):
    """Verstuur resultaten per email."""
    try:
        msg = Message(
            'Uw AI Governance Assessment Resultaten',
            recipients=[email]
        )

        # HTML email body
        msg.html = render_template('email_results.html',
                                   results=results,
                                   recommendations=recommendations)

        mail.send(msg)
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

@app.route('/')
def index():
    """Startpagina met introductie."""
    return render_template('index.html')

@app.route('/assessment')
def assessment():
    """Assessment pagina met vragen."""
    return render_template('assessment.html', questions=ASSESSMENT_QUESTIONS)

@app.route('/submit', methods=['POST'])
def submit():
    """Verwerk assessment submission."""
    try:
        data = request.get_json()
        answers = data.get('answers', {})
        email = data.get('email', '')

        if not email:
            return jsonify({'error': 'Email is verplicht'}), 400

        if len(answers) != len(ASSESSMENT_QUESTIONS):
            return jsonify({'error': 'Niet alle vragen zijn beantwoord'}), 400

        # Bereken resultaten
        results = calculate_results(answers)
        recommendations = get_recommendations(results)

        # Verstuur email
        email_sent = send_results_email(email, results, recommendations)

        # Store in session voor results pagina
        session['results'] = results
        session['recommendations'] = recommendations
        session['email_sent'] = email_sent

        return jsonify({
            'success': True,
            'email_sent': email_sent,
            'results_url': '/results'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/results')
def results():
    """Toon resultaten pagina."""
    results = session.get('results')
    recommendations = session.get('recommendations')
    email_sent = session.get('email_sent', False)

    if not results:
        return redirect('/')

    return render_template('results.html',
                         results=results,
                         recommendations=recommendations,
                         email_sent=email_sent)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

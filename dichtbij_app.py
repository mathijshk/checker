"""
AI-Dichtbij Framework - Interactieve Web Applicatie
Voor verantwoord werken met AI in maatschappelijke organisaties
"""

from flask import Flask, render_template, request, jsonify, session, send_file
import os
import secrets
from datetime import datetime
import json

app = Flask(__name__,
            template_folder='dichtbij_templates',
            static_folder='dichtbij_static')
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(16))

# Framework data structuur
FRAMEWORK_DATA = {
    'waarden': {
        'title': 'Waarden',
        'subtitle': 'Het morele kompas',
        'description': 'AI verantwoord inzetten betekent: bewust kiezen waar AI helpt, begrenzen waar het schaadt, en organiseren wie verantwoordelijk is.',
        'principles': [
            {
                'name': 'Mens blijft eindverantwoordelijk',
                'description': 'AI ondersteunt besluitvorming, maar neemt geen besluiten over mensen zonder menselijke toets.'
            },
            {
                'name': 'Doel vóór middel',
                'description': 'AI wordt alleen ingezet als het het maatschappelijke doel versterkt, niet omdat het goedkoper, sneller of modieus is.'
            },
            {
                'name': 'Transparantie en uitlegbaarheid',
                'description': 'De organisatie kan uitleggen dát AI wordt gebruikt, waarvoor en met welke grenzen, richting medewerkers, cliënten en publiek.'
            },
            {
                'name': 'Gelijkheid en inclusie',
                'description': 'AI mag bestaande ongelijkheid niet versterken en geen nieuwe uitsluiting creëren.'
            },
            {
                'name': 'Zorgvuldigheid boven snelheid',
                'description': 'Experimenteren mag, maar altijd bewust, begrensd en reflectief.'
            }
        ],
        'questions': [
            'Welke van deze waarden zijn al verankerd in uw organisatie?',
            'Welke waarde vraagt in uw context de meeste aandacht?',
            'Hoe zou u deze waarden concreet maken voor uw medewerkers?'
        ]
    },
    'risico': {
        'title': 'Risicologica',
        'subtitle': 'Waar kan het misgaan',
        'description': 'Zes kernrisico\'s die altijd besproken moeten worden bij AI-inzet.',
        'risks': [
            {
                'name': 'Besluitrisico',
                'description': 'Wordt AI gebruikt bij selectie, beoordeling, prioritering of toekenning?',
                'examples': 'Denk aan: prioritering van cliënten, selectie van sollicitanten, toekenning van voorzieningen'
            },
            {
                'name': 'Privacy en data',
                'description': 'Gaat er gevoelige of herleidbare informatie in AI-systemen?',
                'examples': 'Denk aan: namen, BSN-nummers, medische gegevens, locatiedata'
            },
            {
                'name': 'Bias en discriminatie',
                'description': 'Worden bepaalde groepen systematisch benadeeld?',
                'examples': 'Denk aan: uitsluiting op basis van postcode, leeftijd, geslacht, afkomst'
            },
            {
                'name': 'Autorisatie en eigenaarschap',
                'description': 'Wie mag AI gebruiken en wie houdt toezicht?',
                'examples': 'Denk aan: wie heeft toegang, wie controleert, wie is eigenaar van de data'
            },
            {
                'name': 'Afhankelijkheid en verarming',
                'description': 'Verdwijnt menselijk vakmanschap of professioneel oordeel?',
                'examples': 'Denk aan: verlies van expertise, verminderde reflectie, automatisering zonder begrip'
            },
            {
                'name': 'Reputatie en vertrouwen',
                'description': 'Hoe ziet dit eruit als het morgen publiek wordt?',
                'examples': 'Denk aan: mediaberichtgeving, vertrouwen van cliënten, publieke verantwoording'
            }
        ],
        'questions': [
            'Welke van deze risico\'s zijn het meest relevant voor uw huidige AI-gebruik?',
            'Zijn er risico\'s die u nog niet had overwogen?',
            'Hoe zou u deze risico\'s systematisch in kaart kunnen brengen?'
        ]
    },
    'gebruik': {
        'title': 'Gebruikscategorieën',
        'subtitle': 'Wat mag wel, wat niet',
        'description': 'Duidelijke zones voor AI-gebruik met concrete voorbeelden.',
        'zones': [
            {
                'name': 'Groene zone - laag risico',
                'color': '#4CAF50',
                'status': 'Toegestaan',
                'examples': [
                    'Teksten herschrijven',
                    'Samenvatten van openbare informatie',
                    'Brainstormen',
                    'Interne notities'
                ]
            },
            {
                'name': 'Oranje zone - verhoogde aandacht',
                'color': '#FF9800',
                'status': 'Alleen met duidelijke afspraken',
                'examples': [
                    'Analyse van dossiers',
                    'Conceptadviezen',
                    'AI-interactie met cliënten of burgers',
                    'Externe publicatie van AI-gegenereerde content'
                ]
            },
            {
                'name': 'Rode zone - niet toegestaan',
                'color': '#F44336',
                'status': 'Niet toegestaan of alleen na expliciet besluit',
                'examples': [
                    'Geautomatiseerde beslissingen over mensen',
                    'Invoer van vertrouwelijke persoonsgegevens in publieke AI-tools',
                    'AI als vervanger van professioneel oordeel in zorg, onderwijs of toezicht'
                ]
            }
        ],
        'questions': [
            'Welke huidige AI-toepassingen in uw organisatie vallen in welke zone?',
            'Zijn er grijze gebieden die verduidelijking nodig hebben?',
            'Hoe zou u deze indeling communiceren naar medewerkers?'
        ]
    },
    'rollen': {
        'title': 'Rollen en Verantwoordelijkheid',
        'subtitle': 'Wie doet wat',
        'description': 'Heldere verantwoordelijkheidsverdeling voor AI-governance.',
        'roles': [
            {
                'name': 'Bestuur en Raad van Toezicht',
                'responsibilities': [
                    'Stelt waarden en kaders vast',
                    'Weet waar AI wordt ingezet',
                    'Vraagt periodiek naar risico\'s en dilemma\'s'
                ]
            },
            {
                'name': 'Directie',
                'responsibilities': [
                    'Vertaalt kaders naar beleid en keuzes',
                    'Beslist over toepassingen met impact',
                    'Borgt leren en reflectie'
                ]
            },
            {
                'name': 'Medewerkers',
                'responsibilities': [
                    'Weten wat wel en niet mag',
                    'Begrijpen waarom',
                    'Kunnen dilemma\'s veilig bespreken'
                ]
            }
        ],
        'questions': [
            'Zijn deze rollen in uw organisatie duidelijk belegd?',
            'Waar liggen eventuele hiaten of onduidelijkheden?',
            'Hoe zou u deze verantwoordelijkheden formaliseren?'
        ]
    },
    'leren': {
        'title': 'Leren en Reflectie',
        'subtitle': 'Verantwoord AI-gebruik is een proces, geen vinkje',
        'description': 'Werkende vormen om continu te leren en verbeteren.',
        'practices': [
            {
                'name': 'Periodieke AI-reflectie',
                'description': 'Regelmatige momenten om stil te staan bij AI-gebruik'
            },
            {
                'name': 'Bespreking van concrete casussen',
                'description': 'Leren van echte situaties en dilemma\'s'
            },
            {
                'name': 'Leren van fouten zonder schuld',
                'description': 'Veilige omgeving om misstappen te delen'
            },
            {
                'name': 'Vast kanaal voor twijfel en signalen',
                'description': 'Toegankelijke weg om zorgen te uiten'
            }
        ],
        'questions': [
            'Welke leervormen passen bij uw organisatiecultuur?',
            'Hoe zou u een veilige omgeving creëren voor het delen van AI-dilemma\'s?',
            'Wie zou het initiatief kunnen nemen voor reflectiemomenten?'
        ]
    },
    'documenten': {
        'title': 'Minimale Set Documenten',
        'subtitle': 'Voldoende is:',
        'description': 'Eenvoudige maar effectieve documentatie voor AI-governance.',
        'documents': [
            {
                'name': 'AI-principes',
                'description': '1 pagina met de kernwaarden van uw organisatie'
            },
            {
                'name': 'Gebruikskaders',
                'description': 'Overzicht van groen, oranje, rood zones'
            },
            {
                'name': 'Rolafspraken',
                'description': 'Wie is waarvoor verantwoordelijk'
            },
            {
                'name': 'Acceptable use-afspraken',
                'description': 'Wat medewerkers wel en niet mogen'
            }
        ],
        'questions': [
            'Welke documenten heeft u al en welke ontbreken nog?',
            'Hoe zou u deze documenten toegankelijk en praktisch kunnen maken?',
            'Wie zou verantwoordelijk zijn voor het opstellen en bijhouden?'
        ]
    }
}

@app.route('/')
def index():
    """Homepage met framework overzicht"""
    return render_template('dichtbij_index.html', framework=FRAMEWORK_DATA)

@app.route('/layer/<layer_id>')
def layer(layer_id):
    """Individuele laag pagina"""
    if layer_id not in FRAMEWORK_DATA:
        return redirect('/')

    layer_data = FRAMEWORK_DATA[layer_id]
    layer_number = list(FRAMEWORK_DATA.keys()).index(layer_id) + 1
    total_layers = len(FRAMEWORK_DATA)

    # Determine previous and next layers
    layer_keys = list(FRAMEWORK_DATA.keys())
    current_index = layer_keys.index(layer_id)
    prev_layer = layer_keys[current_index - 1] if current_index > 0 else None
    next_layer = layer_keys[current_index + 1] if current_index < len(layer_keys) - 1 else None

    return render_template('dichtbij_layer.html',
                         layer_id=layer_id,
                         layer_data=layer_data,
                         layer_number=layer_number,
                         total_layers=total_layers,
                         prev_layer=prev_layer,
                         next_layer=next_layer)

@app.route('/assessment')
def assessment():
    """Volledige assessment pagina"""
    return render_template('dichtbij_assessment.html', framework=FRAMEWORK_DATA)

@app.route('/api/save-responses', methods=['POST'])
def save_responses():
    """Opslaan van gebruikersresponsen"""
    data = request.json
    session['responses'] = data
    session['timestamp'] = datetime.now().isoformat()
    return jsonify({'status': 'success'})

@app.route('/api/generate-action-plan', methods=['POST'])
def generate_action_plan():
    """Genereer actieplan op basis van responses"""
    responses = request.json.get('responses', {})

    action_plan = {
        'timestamp': datetime.now().isoformat(),
        'priorities': [],
        'quick_wins': [],
        'long_term': []
    }

    # Analyseer responses en genereer aanbevelingen
    for layer_id, layer_responses in responses.items():
        if layer_id in FRAMEWORK_DATA:
            layer_data = FRAMEWORK_DATA[layer_id]

            # Bepaal prioriteiten op basis van responses
            for question_idx, answer in enumerate(layer_responses.get('answers', [])):
                if answer and answer.strip():
                    # Check voor keywords die urgentie aangeven
                    urgent_keywords = ['nog niet', 'geen', 'onduidelijk', 'probleem', 'risico']
                    is_urgent = any(keyword in answer.lower() for keyword in urgent_keywords)

                    if is_urgent:
                        action_plan['priorities'].append({
                            'layer': layer_data['title'],
                            'area': layer_data.get('questions', [])[question_idx] if question_idx < len(layer_data.get('questions', [])) else 'Algemeen',
                            'action': f"Aandacht nodig voor: {answer[:100]}..."
                        })

    # Genereer quick wins
    if not responses.get('documenten'):
        action_plan['quick_wins'].append({
            'title': 'Start met AI-principes',
            'description': 'Maak een 1-pager met uw AI-waarden',
            'effort': 'Laag'
        })

    if not responses.get('gebruik'):
        action_plan['quick_wins'].append({
            'title': 'Definieer gebruikszones',
            'description': 'Bepaal wat groen, oranje en rood is voor uw organisatie',
            'effort': 'Laag'
        })

    # Lange termijn acties
    action_plan['long_term'].append({
        'title': 'Implementeer structurele reflectie',
        'description': 'Creëer vaste momenten voor AI-reflectie en leren',
        'timeline': '3-6 maanden'
    })

    action_plan['long_term'].append({
        'title': 'Formaliseer governance structuur',
        'description': 'Belegd rollen en verantwoordelijkheden formeel',
        'timeline': '6-12 maanden'
    })

    return jsonify(action_plan)

@app.route('/results')
def results():
    """Resultaten pagina met actieplan"""
    responses = session.get('responses', {})
    if not responses:
        return redirect('/assessment')

    return render_template('dichtbij_results.html',
                         responses=responses,
                         framework=FRAMEWORK_DATA)

if __name__ == '__main__':
    # Maak directories aan als ze niet bestaan
    os.makedirs('dichtbij_templates', exist_ok=True)
    os.makedirs('dichtbij_static', exist_ok=True)

    app.run(debug=True, host='0.0.0.0', port=5001)

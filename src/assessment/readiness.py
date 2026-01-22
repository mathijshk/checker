"""
AI Readiness Assessment Module

Dit module helpt organisaties hun AI-gereedheid te beoordelen.
"""

class AIReadinessAssessment:
    """Beoordeelt de AI-gereedheid van een organisatie."""

    def __init__(self):
        self.categories = {
            "Strategie": [
                "Heeft uw organisatie een duidelijke AI-strategie?",
                "Is AI opgenomen in de bedrijfsstrategie?",
                "Zijn er concrete AI-doelstellingen gedefinieerd?"
            ],
            "Data & Infrastructuur": [
                "Beschikt uw organisatie over voldoende kwalitatieve data?",
                "Is de data-infrastructuur geschikt voor AI-toepassingen?",
                "Wordt data governance toegepast?"
            ],
            "Talent & Skills": [
                "Heeft uw organisatie voldoende AI-expertise in huis?",
                "Zijn er trainingen voor AI-geletterdheid?",
                "Is er een plan voor het aantrekken van AI-talent?"
            ],
            "Governance & Ethiek": [
                "Zijn er governance structuren voor AI-projecten?",
                "Heeft uw organisatie ethische richtlijnen voor AI?",
                "Is er een verantwoordelijke aangesteld voor AI-governance?"
            ],
            "Technologie": [
                "Heeft uw organisatie de benodigde technische infrastructuur?",
                "Worden moderne AI-tools en -platforms gebruikt?",
                "Is er budget gealloceerd voor AI-technologie?"
            ]
        }
        self.answers = {}
        self.scores = {}

    def _ask_question(self, question):
        """Stel een vraag en krijg een score van 1-5."""
        while True:
            print(f"\n{question}")
            print("Score: 1 (Helemaal niet) - 5 (Volledig)")
            try:
                score = input("Uw score (1-5): ").strip()
                score = int(score)
                if 1 <= score <= 5:
                    return score
                else:
                    print("⚠ Voer een getal tussen 1 en 5 in.")
            except ValueError:
                print("⚠ Voer een geldig getal in.")

    def calculate_score(self, answers):
        """Bereken de gereedheidscore per categorie."""
        scores = {}
        for category, category_answers in answers.items():
            avg_score = sum(category_answers) / len(category_answers)
            scores[category] = round(avg_score, 1)
        return scores

    def generate_recommendations(self, scores):
        """Genereer aanbevelingen gebaseerd op scores."""
        recommendations = {}

        for category, score in scores.items():
            if score < 2.0:
                level = "Kritiek"
                recs = [
                    f"Urgente actie nodig voor {category}",
                    "Start met een baseline assessment",
                    "Alloceer budget en resources"
                ]
            elif score < 3.0:
                level = "Ontwikkelend"
                recs = [
                    f"Versterk {category} met gerichte investeringen",
                    "Ontwikkel een verbeterplan",
                    "Zoek externe expertise indien nodig"
                ]
            elif score < 4.0:
                level = "Gevorderd"
                recs = [
                    f"Optimaliseer {category} verder",
                    "Deel best practices binnen de organisatie",
                    "Monitor voortgang regelmatig"
                ]
            else:
                level = "Excellent"
                recs = [
                    f"{category} is op niveau",
                    "Blijf best practices toepassen",
                    "Deel kennis met andere afdelingen"
                ]

            recommendations[category] = {
                'level': level,
                'recommendations': recs
            }

        return recommendations

    def run_assessment(self):
        """Voer de volledige assessment uit."""
        print("\nDeze assessment helpt u de AI-gereedheid van uw organisatie te meten.")
        print(f"Er zijn {len(self.categories)} categorieën met elk 3 vragen.\n")

        for category, questions in self.categories.items():
            print(f"\n{'='*60}")
            print(f"CATEGORIE: {category.upper()}")
            print('='*60)

            category_answers = []
            for i, question in enumerate(questions, 1):
                print(f"\nVraag {i}/{len(questions)}")
                score = self._ask_question(question)
                category_answers.append(score)

            self.answers[category] = category_answers

        # Bereken scores
        self.scores = self.calculate_score(self.answers)

        # Toon resultaten
        print("\n" + "="*60)
        print("ASSESSMENT RESULTATEN")
        print("="*60)

        total_score = sum(self.scores.values()) / len(self.scores)

        for category, score in self.scores.items():
            bar = "█" * int(score) + "░" * (5 - int(score))
            print(f"\n{category:.<30} {score:.1f}/5.0  [{bar}]")

        print(f"\n{'='*60}")
        print(f"TOTAAL GEMIDDELDE: {total_score:.1f}/5.0")
        print('='*60)

        # Genereer aanbevelingen
        recommendations = self.generate_recommendations(self.scores)

        print("\n" + "="*60)
        print("AANBEVELINGEN")
        print("="*60)

        for category, rec_data in recommendations.items():
            print(f"\n{category} - {rec_data['level']}")
            for rec in rec_data['recommendations']:
                print(f"  • {rec}")

        return self.scores

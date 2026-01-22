"""
AI Governance Framework

Module voor het implementeren van AI governance best practices.
"""

class AIGovernanceFramework:
    """Framework voor AI governance binnen organisaties."""

    def __init__(self):
        self.principles = {
            "Transparantie": [
                "Zijn AI-beslissingen uitlegbaar aan stakeholders?",
                "Is er documentatie over hoe AI-systemen werken?",
                "Worden gebruikers geïnformeerd over AI-gebruik?"
            ],
            "Verantwoordelijkheid": [
                "Is er een verantwoordelijke persoon voor elk AI-systeem?",
                "Zijn rollen en verantwoordelijkheden duidelijk gedefinieerd?",
                "Is er een escalatieproces bij AI-gerelateerde incidenten?"
            ],
            "Eerlijkheid": [
                "Worden AI-systemen getest op bias en discriminatie?",
                "Is er diversiteit in de data en ontwikkelteams?",
                "Zijn er processen om oneerlijke uitkomsten te corrigeren?"
            ],
            "Privacy": [
                "Voldoet AI-gebruik aan AVG/GDPR?",
                "Wordt privacy by design toegepast?",
                "Zijn er privacy impact assessments uitgevoerd?"
            ],
            "Veiligheid": [
                "Zijn AI-systemen beveiligd tegen aanvallen?",
                "Worden risico's proactief geïdentificeerd en gemitigeerd?",
                "Is er een incident response plan voor AI-systemen?"
            ]
        }
        self.maturity_levels = {
            1: "Initieel - Ad hoc, geen formele processen",
            2: "Beheerd - Basis processen aanwezig",
            3: "Gedefinieerd - Gedocumenteerde standaarden",
            4: "Kwantitatief - Meetbare processen",
            5: "Optimaliseren - Continue verbetering"
        }
        self.assessment_results = {}

    def assess_governance_maturity(self):
        """Beoordeel de governance volwassenheid van een organisatie."""
        print("\nDeze analyse beoordeelt de AI governance volwassenheid van uw organisatie.")
        print(f"We evalueren {len(self.principles)} governance principes.\n")

        principle_scores = {}

        for principle, questions in self.principles.items():
            print(f"\n{'='*60}")
            print(f"PRINCIPE: {principle.upper()}")
            print('='*60)

            scores = []
            for i, question in enumerate(questions, 1):
                print(f"\nVraag {i}/{len(questions)}")
                print(f"{question}")
                print("\nMaturity level:")
                print("1 = Helemaal niet / Ad hoc")
                print("2 = Basis niveau")
                print("3 = Goed gedefinieerd")
                print("4 = Meetbaar en gecontroleerd")
                print("5 = Excellent / Continue optimalisatie")

                while True:
                    try:
                        score = int(input("\nUw score (1-5): ").strip())
                        if 1 <= score <= 5:
                            scores.append(score)
                            break
                        print("⚠ Voer een getal tussen 1 en 5 in.")
                    except ValueError:
                        print("⚠ Voer een geldig getal in.")

            avg_score = sum(scores) / len(scores)
            principle_scores[principle] = round(avg_score, 1)

        # Bereken overall maturity
        overall_score = sum(principle_scores.values()) / len(principle_scores)
        overall_level = round(overall_score)

        self.assessment_results = {
            'principle_scores': principle_scores,
            'overall_score': round(overall_score, 1),
            'maturity_level': overall_level,
            'maturity_description': self.maturity_levels[overall_level]
        }

        # Toon resultaten
        print(f"\n{'='*60}")
        print("GOVERNANCE MATURITY RESULTATEN")
        print('='*60)

        for principle, score in principle_scores.items():
            bar = "█" * int(score) + "░" * (5 - int(score))
            print(f"\n{principle:.<30} {score:.1f}/5.0  [{bar}]")

        print(f"\n{'='*60}")
        print(f"OVERALL MATURITY LEVEL: {overall_level}/5")
        print(f"{self.maturity_levels[overall_level]}")
        print('='*60)

        return self.assessment_results

    def get_best_practices(self, maturity_level):
        """Haal best practices op voor het verbeteren van governance."""
        recommendations = {
            1: [
                "Start met het aanwijzen van een AI governance verantwoordelijke",
                "Maak een inventarisatie van alle AI-systemen in gebruik",
                "Ontwikkel een basis AI ethics statement",
                "Organiseer awareness sessies over verantwoorde AI"
            ],
            2: [
                "Formaliseer AI governance processen en documenteer deze",
                "Implementeer een AI project approval proces",
                "Start met risico assessments voor AI-projecten",
                "Creëer een AI governance committee"
            ],
            3: [
                "Implementeer gestandaardiseerde AI impact assessments",
                "Ontwikkel een AI risk management framework",
                "Integreer AI governance in bestaande governance structuren",
                "Train medewerkers in verantwoorde AI ontwikkeling"
            ],
            4: [
                "Implementeer KPI's voor AI governance",
                "Voer regelmatige audits uit op AI-systemen",
                "Automatiseer compliance monitoring waar mogelijk",
                "Benchmark tegen industry standards"
            ],
            5: [
                "Blijf innoveren in AI governance praktijken",
                "Deel best practices met de industrie",
                "Anticipeer op toekomstige regelgeving",
                "Investeer in research naar verantwoorde AI"
            ]
        }
        return recommendations.get(maturity_level, [])

    def run_analysis(self):
        """Voer een volledige governance analyse uit."""
        # Voer maturity assessment uit
        results = self.assess_governance_maturity()

        # Haal best practices op
        print(f"\n{'='*60}")
        print("AANBEVELINGEN")
        print('='*60)
        print(f"\nOm uw governance naar het volgende niveau te brengen:")
        print()

        next_level = min(results['maturity_level'] + 1, 5)
        practices = self.get_best_practices(next_level)

        for i, practice in enumerate(practices, 1):
            print(f"{i}. {practice}")

        # Principe-specifieke aanbevelingen
        print(f"\n{'='*60}")
        print("PRINCIPE-SPECIFIEKE AANBEVELINGEN")
        print('='*60)

        for principle, score in results['principle_scores'].items():
            if score < 3.0:
                print(f"\n⚠ {principle} (Score: {score:.1f}/5.0)")
                print(f"  → Prioriteit: Dit principe vereist directe aandacht")
                if principle == "Transparantie":
                    print("  → Start met het documenteren van AI-beslissingsprocessen")
                elif principle == "Verantwoordelijkheid":
                    print("  → Wijs duidelijke eigenaren toe aan AI-systemen")
                elif principle == "Eerlijkheid":
                    print("  → Implementeer bias testing in uw AI development proces")
                elif principle == "Privacy":
                    print("  → Voer een DPIA uit voor alle AI-systemen met persoonsgegevens")
                elif principle == "Veiligheid":
                    print("  → Ontwikkel een AI-specifiek security framework")

        return results['maturity_level']

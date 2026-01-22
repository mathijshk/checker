"""
AI Governance Checker - Main Entry Point

Hoofdprogramma voor de AI governance tool voor directeuren en bestuurders.
"""

import sys
from src.assessment.readiness import AIReadinessAssessment
from src.compliance.ai_act_checker import AIActChecker
from src.governance.framework import AIGovernanceFramework
from src.reports.generator import ReportGenerator


class AIGovernanceApp:
    """Hoofdapplicatie voor AI Governance Checker."""

    def __init__(self):
        self.assessment = AIReadinessAssessment()
        self.compliance = AIActChecker()
        self.governance = AIGovernanceFramework()
        self.report_gen = ReportGenerator()
        self.session_data = {
            'assessment_scores': None,
            'compliance_results': None,
            'governance_level': None
        }

    def show_menu(self):
        """Toon het hoofdmenu."""
        print("\n" + "=" * 60)
        print("AI Governance Checker - Hoofdmenu")
        print("=" * 60)
        print("\n1. AI Readiness Assessment")
        print("2. AI Act Compliance Checker")
        print("3. Governance Framework Analyse")
        print("4. Genereer Directierapport")
        print("5. Toon Huidige Sessie Data")
        print("6. Exit")
        print()

    def run_assessment(self):
        """Voer AI readiness assessment uit."""
        print("\n" + "=" * 60)
        print("AI READINESS ASSESSMENT")
        print("=" * 60)
        scores = self.assessment.run_assessment()
        self.session_data['assessment_scores'] = scores

        print(f"\n✓ Assessment voltooid. Scores opgeslagen.")
        input("\nDruk op Enter om verder te gaan...")

    def run_compliance_check(self):
        """Voer AI Act compliance check uit."""
        print("\n" + "=" * 60)
        print("AI ACT COMPLIANCE CHECKER")
        print("=" * 60)
        results = self.compliance.run_compliance_check()
        self.session_data['compliance_results'] = results

        print(f"\n✓ Compliance check voltooid. Resultaten opgeslagen.")
        input("\nDruk op Enter om verder te gaan...")

    def run_governance_analysis(self):
        """Voer governance framework analyse uit."""
        print("\n" + "=" * 60)
        print("GOVERNANCE FRAMEWORK ANALYSE")
        print("=" * 60)
        level = self.governance.run_analysis()
        self.session_data['governance_level'] = level

        print(f"\n✓ Governance analyse voltooid. Resultaten opgeslagen.")
        input("\nDruk op Enter om verder te gaan...")

    def generate_report(self):
        """Genereer directierapport."""
        print("\n" + "=" * 60)
        print("DIRECTIERAPPORT GENEREREN")
        print("=" * 60)

        if not any(self.session_data.values()):
            print("\n⚠ Er is nog geen data verzameld.")
            print("Voer eerst één of meer assessments uit.")
            input("\nDruk op Enter om verder te gaan...")
            return

        print("\nGenereer rapport met beschikbare data...")
        report = self.report_gen.generate_executive_summary(
            self.session_data['assessment_scores'],
            self.session_data['compliance_results']
        )

        filename = input("\nBestandsnaam voor rapport (zonder extensie): ").strip()
        if not filename:
            filename = "directierapport"

        try:
            saved_path = self.report_gen.save_report(report, filename)
            print(f"\n✓ Rapport opgeslagen: {saved_path}")
        except Exception as e:
            print(f"\n✗ Fout bij opslaan rapport: {e}")

        input("\nDruk op Enter om verder te gaan...")

    def show_session_data(self):
        """Toon huidige sessie data."""
        print("\n" + "=" * 60)
        print("HUIDIGE SESSIE DATA")
        print("=" * 60)

        print("\n1. Assessment Scores:")
        if self.session_data['assessment_scores']:
            for cat, score in self.session_data['assessment_scores'].items():
                print(f"   - {cat}: {score}/5")
        else:
            print("   Nog niet uitgevoerd")

        print("\n2. AI Act Compliance:")
        if self.session_data['compliance_results']:
            print(f"   - Risico Niveau: {self.session_data['compliance_results']['risk_level']}")
            print(f"   - Compliant: {'Ja' if self.session_data['compliance_results']['compliant'] else 'Nee'}")
        else:
            print("   Nog niet uitgevoerd")

        print("\n3. Governance Niveau:")
        if self.session_data['governance_level']:
            print(f"   - Niveau: {self.session_data['governance_level']}")
        else:
            print("   Nog niet uitgevoerd")

        input("\n\nDruk op Enter om verder te gaan...")

    def run(self):
        """Start de applicatie."""
        print("\n" + "=" * 60)
        print("Welkom bij AI Governance Checker")
        print("=" * 60)
        print("\nDeze tool helpt u met:")
        print("• AI-geletterdheid voor directie en bestuur")
        print("• EU AI Act compliance")
        print("• Governance best practices")
        print("\nLaten we beginnen!")
        input("\nDruk op Enter om verder te gaan...")

        while True:
            self.show_menu()
            choice = input("Maak uw keuze (1-6): ").strip()

            if choice == '1':
                self.run_assessment()
            elif choice == '2':
                self.run_compliance_check()
            elif choice == '3':
                self.run_governance_analysis()
            elif choice == '4':
                self.generate_report()
            elif choice == '5':
                self.show_session_data()
            elif choice == '6':
                print("\n" + "=" * 60)
                print("Bedankt voor het gebruiken van AI Governance Checker!")
                print("=" * 60)
                print()
                break
            else:
                print("\n⚠ Ongeldige keuze. Probeer opnieuw.")
                input("Druk op Enter om verder te gaan...")


def main():
    """Hoofdfunctie voor de applicatie."""
    app = AIGovernanceApp()
    app.run()


if __name__ == "__main__":
    main()

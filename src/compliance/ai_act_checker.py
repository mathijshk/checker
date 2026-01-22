"""
AI Act Compliance Checker

Module om AI systemen te controleren op compliance met de EU AI Act.
"""

class AIActChecker:
    """Controleert AI systemen op EU AI Act compliance."""

    # AI Act risk categorieën
    RISK_LEVELS = {
        "UNACCEPTABLE": "Verboden systemen",
        "HIGH": "Hoog-risico systemen",
        "LIMITED": "Beperkt risico",
        "MINIMAL": "Minimaal risico"
    }

    def __init__(self):
        self.risk_level = None
        self.requirements = []
        self.system_info = {}

    def classify_risk_level(self, use_case):
        """Classificeer het risico niveau van een AI systeem."""
        # Verboden toepassingen
        forbidden_keywords = ['social scoring', 'manipulatie', 'biometric identification real-time']

        # Hoog-risico toepassingen
        high_risk_keywords = [
            'recruitment', 'werving', 'selectie', 'hr',
            'krediet', 'credit scoring', 'financieel',
            'medisch', 'healthcare', 'diagnose',
            'onderwijs', 'education', 'exam',
            'law enforcement', 'rechtshandhaving',
            'biometric', 'biometrisch',
            'critical infrastructure', 'kritieke infrastructuur'
        ]

        use_case_lower = use_case.lower()

        # Check voor verboden systemen
        for keyword in forbidden_keywords:
            if keyword in use_case_lower:
                return "UNACCEPTABLE"

        # Check voor hoog-risico systemen
        for keyword in high_risk_keywords:
            if keyword in use_case_lower:
                return "HIGH"

        # Check voor beperkt risico (chatbots, deepfakes)
        if any(word in use_case_lower for word in ['chatbot', 'chat', 'deepfake', 'synthetic media']):
            return "LIMITED"

        # Anders minimaal risico
        return "MINIMAL"

    def get_requirements(self, risk_level):
        """Haal de toepasselijke vereisten op voor een risico niveau."""
        requirements = {
            "UNACCEPTABLE": [
                "❌ Dit systeem is VERBODEN onder de EU AI Act",
                "❌ Gebruik van dit systeem is niet toegestaan",
                "⚠ Onmiddellijke stopzetting vereist"
            ],
            "HIGH": [
                "Risk management systeem implementeren",
                "Data governance en kwaliteitseisen",
                "Technische documentatie bijhouden",
                "Automatische logging van gebeurtenissen",
                "Menselijk toezicht waarborgen",
                "Robuustheid en nauwkeurigheid garanderen",
                "Cybersecurity maatregelen",
                "Conformiteitsbeoordeling uitvoeren",
                "CE-markering aanbrengen",
                "Registratie in EU database"
            ],
            "LIMITED": [
                "Transparantieverplichting: gebruikers informeren",
                "Duidelijk maken dat ze met AI interacteren",
                "Mogelijkheid tot menselijk contact bieden"
            ],
            "MINIMAL": [
                "Vrijwillige gedragscodes volgen (optioneel)",
                "Best practices voor verantwoorde AI toepassen"
            ]
        }
        return requirements.get(risk_level, [])

    def check_compliance(self, requirements):
        """Controleer of een systeem voldoet aan de vereisten."""
        compliance_status = {}

        if self.risk_level == "UNACCEPTABLE":
            return {
                'compliant': False,
                'critical': True,
                'message': 'Dit systeem is verboden onder de EU AI Act'
            }

        print(f"\n{'='*60}")
        print(f"COMPLIANCE CHECK - {self.RISK_LEVELS[self.risk_level]}")
        print('='*60)
        print("\nControleer de volgende vereisten:\n")

        met_requirements = 0
        total_requirements = len(requirements)

        for i, req in enumerate(requirements, 1):
            print(f"{i}. {req}")
            while True:
                response = input("   Voldaan? (j/n): ").strip().lower()
                if response in ['j', 'n']:
                    compliance_status[req] = (response == 'j')
                    if response == 'j':
                        met_requirements += 1
                    break
                print("   ⚠ Voer 'j' of 'n' in.")

        compliant = met_requirements == total_requirements
        compliance_percentage = (met_requirements / total_requirements * 100) if total_requirements > 0 else 100

        return {
            'compliant': compliant,
            'met_requirements': met_requirements,
            'total_requirements': total_requirements,
            'percentage': compliance_percentage,
            'details': compliance_status
        }

    def run_compliance_check(self):
        """Voer een volledige compliance check uit."""
        print("\nDeze module helpt u te controleren of uw AI-systeem voldoet aan de EU AI Act.\n")

        # Stap 1: Verzamel systeem informatie
        print("STAP 1: SYSTEEM INFORMATIE")
        print("-" * 60)
        system_name = input("\nNaam van het AI-systeem: ").strip()
        use_case = input("Beschrijf de toepassing/use case: ").strip()
        provider = input("Aanbieder/ontwikkelaar: ").strip()

        self.system_info = {
            'name': system_name,
            'use_case': use_case,
            'provider': provider
        }

        # Stap 2: Classificeer risico niveau
        print(f"\n{'='*60}")
        print("STAP 2: RISICO CLASSIFICATIE")
        print('='*60)

        self.risk_level = self.classify_risk_level(use_case)
        risk_description = self.RISK_LEVELS[self.risk_level]

        print(f"\n✓ Risico niveau: {self.risk_level}")
        print(f"  ({risk_description})")

        # Stap 3: Haal vereisten op
        print(f"\n{'='*60}")
        print("STAP 3: TOEPASSELIJKE VEREISTEN")
        print('='*60)

        requirements = self.get_requirements(self.risk_level)
        self.requirements = requirements

        if self.risk_level == "UNACCEPTABLE":
            print("\n⚠ WAARSCHUWING: Dit is een verboden AI-systeem!")
            for req in requirements:
                print(f"  {req}")
            return {
                'system_name': system_name,
                'risk_level': self.risk_level,
                'compliant': False,
                'forbidden': True
            }

        # Stap 4: Check compliance
        print(f"\n{'='*60}")
        print("STAP 4: COMPLIANCE VERIFICATIE")
        print('='*60)

        compliance_result = self.check_compliance(requirements)

        # Toon resultaten
        print(f"\n{'='*60}")
        print("COMPLIANCE RESULTAAT")
        print('='*60)

        print(f"\nSysteem: {system_name}")
        print(f"Risico Niveau: {self.risk_level} ({risk_description})")
        print(f"\nVereisten voldaan: {compliance_result['met_requirements']}/{compliance_result['total_requirements']}")
        print(f"Compliance: {compliance_result['percentage']:.0f}%")

        if compliance_result['compliant']:
            print("\n✓ Het systeem voldoet aan alle AI Act vereisten!")
        else:
            print(f"\n✗ Het systeem voldoet NIET aan alle vereisten.")
            print("  Actie vereist voor niet-voldane punten.")

        return {
            'system_name': system_name,
            'risk_level': self.risk_level,
            'compliant': compliance_result['compliant'],
            'percentage': compliance_result['percentage'],
            'requirements': requirements,
            'details': compliance_result['details']
        }

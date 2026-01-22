"""
Demo script voor AI Governance Checker

Dit script demonstreert de functionaliteit zonder interactieve input.
"""

from src.assessment.readiness import AIReadinessAssessment
from src.compliance.ai_act_checker import AIActChecker
from src.governance.framework import AIGovernanceFramework
from src.reports.generator import ReportGenerator


def demo_assessment():
    """Demonstreer AI Readiness Assessment met voorbeelddata."""
    print("\n" + "=" * 70)
    print("DEMO: AI READINESS ASSESSMENT")
    print("=" * 70)

    assessment = AIReadinessAssessment()

    # Simuleer antwoorden
    example_answers = {
        "Strategie": [3, 4, 3],
        "Data & Infrastructuur": [4, 4, 3],
        "Talent & Skills": [2, 2, 3],
        "Governance & Ethiek": [3, 3, 2],
        "Technologie": [4, 3, 3]
    }

    print("\nVoorbeeld antwoorden (scores 1-5):")
    for category, answers in example_answers.items():
        avg = sum(answers) / len(answers)
        print(f"  {category}: {answers} → Gemiddelde: {avg:.1f}")

    # Bereken scores
    scores = assessment.calculate_score(example_answers)

    print("\n" + "=" * 70)
    print("RESULTATEN")
    print("=" * 70)

    total_score = sum(scores.values()) / len(scores)

    for category, score in scores.items():
        bar = "█" * int(score) + "░" * (5 - int(score))
        print(f"\n{category:.<35} {score:.1f}/5.0  [{bar}]")

    print(f"\n{'=' * 70}")
    print(f"TOTAAL GEMIDDELDE: {total_score:.1f}/5.0")
    print('=' * 70)

    # Genereer aanbevelingen
    recommendations = assessment.generate_recommendations(scores)

    print("\n" + "=" * 70)
    print("AANBEVELINGEN")
    print("=" * 70)

    for category, rec_data in recommendations.items():
        print(f"\n{category} - Niveau: {rec_data['level']}")
        for rec in rec_data['recommendations']:
            print(f"  • {rec}")

    return scores


def demo_compliance():
    """Demonstreer AI Act Compliance Checker."""
    print("\n\n" + "=" * 70)
    print("DEMO: AI ACT COMPLIANCE CHECKER")
    print("=" * 70)

    checker = AIActChecker()

    # Test verschillende use cases
    test_cases = [
        {
            'name': 'HR Recruitment AI',
            'use_case': 'AI-systeem voor werving en selectie van kandidaten',
            'expected_risk': 'HIGH'
        },
        {
            'name': 'Customer Service Chatbot',
            'use_case': 'Chatbot voor klantenservice vragen',
            'expected_risk': 'LIMITED'
        },
        {
            'name': 'Marketing Analytics',
            'use_case': 'AI voor marketing data analyse',
            'expected_risk': 'MINIMAL'
        }
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\n{'-' * 70}")
        print(f"Test Case {i}: {test['name']}")
        print(f"{'-' * 70}")
        print(f"Use case: {test['use_case']}")

        risk_level = checker.classify_risk_level(test['use_case'])
        risk_description = checker.RISK_LEVELS[risk_level]
        requirements = checker.get_requirements(risk_level)

        print(f"\n✓ Risico Niveau: {risk_level}")
        print(f"  ({risk_description})")
        print(f"  Verwacht: {test['expected_risk']}")
        print(f"  ✓ Match!" if risk_level == test['expected_risk'] else f"  ✗ Verschil")

        print(f"\nAantal vereisten: {len(requirements)}")
        print("Vereisten:")
        for j, req in enumerate(requirements[:3], 1):  # Toon eerste 3
            print(f"  {j}. {req}")
        if len(requirements) > 3:
            print(f"  ... en {len(requirements) - 3} meer")

    # Return data voor rapport
    return {
        'system_name': 'HR Recruitment AI',
        'risk_level': 'HIGH',
        'compliant': False,
        'percentage': 70.0,
        'requirements': checker.get_requirements('HIGH'),
        'details': {}
    }


def demo_governance():
    """Demonstreer Governance Framework."""
    print("\n\n" + "=" * 70)
    print("DEMO: GOVERNANCE FRAMEWORK ANALYSE")
    print("=" * 70)

    framework = AIGovernanceFramework()

    # Simuleer scores
    example_scores = {
        "Transparantie": 3.3,
        "Verantwoordelijkheid": 3.7,
        "Eerlijkheid": 2.7,
        "Privacy": 4.0,
        "Veiligheid": 3.3
    }

    print("\nVoorbeeld governance scores:")

    overall_score = sum(example_scores.values()) / len(example_scores)
    overall_level = round(overall_score)

    for principle, score in example_scores.items():
        bar = "█" * int(score) + "░" * (5 - int(score))
        print(f"\n{principle:.<35} {score:.1f}/5.0  [{bar}]")

    print(f"\n{'=' * 70}")
    print(f"OVERALL MATURITY LEVEL: {overall_level}/5")
    print(f"{framework.maturity_levels[overall_level]}")
    print('=' * 70)

    # Best practices
    print(f"\n{' AANBEVELINGEN ':-^70}")
    print(f"\nOm uw governance naar niveau {overall_level + 1} te brengen:")

    next_level = min(overall_level + 1, 5)
    practices = framework.get_best_practices(next_level)

    for i, practice in enumerate(practices, 1):
        print(f"{i}. {practice}")

    # Principe-specifieke aanbevelingen
    print(f"\n{' PRINCIPE-SPECIFIEKE AANBEVELINGEN ':-^70}")

    for principle, score in example_scores.items():
        if score < 3.0:
            print(f"\n⚠ {principle} (Score: {score:.1f}/5.0)")
            print(f"  → Prioriteit: Dit principe vereist directe aandacht")

    return overall_level


def demo_report(assessment_scores, compliance_data):
    """Demonstreer rapport generatie."""
    print("\n\n" + "=" * 70)
    print("DEMO: DIRECTIERAPPORT GENERATIE")
    print("=" * 70)

    generator = ReportGenerator()

    print("\nGenereer executive summary met verzamelde data...")
    report = generator.generate_executive_summary(assessment_scores, compliance_data)

    print("\n" + "=" * 70)
    print("RAPPORT PREVIEW (eerste 50 regels)")
    print("=" * 70)

    report_lines = report.split('\n')
    for i, line in enumerate(report_lines[:50], 1):
        print(line)

    if len(report_lines) > 50:
        print(f"\n... en {len(report_lines) - 50} meer regels")

    # Sla rapport op
    print("\n" + "=" * 70)
    filename = "demo_rapport"
    try:
        saved_path = generator.save_report(report, filename)
        print(f"✓ Rapport opgeslagen: {saved_path}")

        # Toon bestandsinfo
        import os
        file_size = os.path.getsize(saved_path)
        print(f"  Bestandsgrootte: {file_size} bytes")
        print(f"  Aantal regels: {len(report_lines)}")

    except Exception as e:
        print(f"✗ Fout bij opslaan: {e}")

    return saved_path


def main():
    """Voer volledige demo uit."""
    print("\n" + "=" * 70)
    print(" " * 15 + "AI GOVERNANCE CHECKER - DEMO")
    print("=" * 70)
    print("\nDeze demo toont alle functionaliteit met voorbeelddata.")
    print("Voor echte sessies, gebruik: python main.py")

    # 1. AI Readiness Assessment
    assessment_scores = demo_assessment()

    # 2. AI Act Compliance
    compliance_data = demo_compliance()

    # 3. Governance Framework
    governance_level = demo_governance()

    # 4. Rapport Generatie
    report_path = demo_report(assessment_scores, compliance_data)

    # Samenvatting
    print("\n\n" + "=" * 70)
    print(" " * 20 + "DEMO SAMENVATTING")
    print("=" * 70)

    print("\n✓ Alle modules succesvol getest:")
    print(f"  • AI Readiness Assessment - Gemiddelde score: {sum(assessment_scores.values()) / len(assessment_scores):.1f}/5.0")
    print(f"  • AI Act Compliance - Risico niveau: {compliance_data['risk_level']}")
    print(f"  • Governance Framework - Maturity level: {governance_level}/5")
    print(f"  • Rapport Generatie - Opgeslagen in: {report_path}")

    print("\n" + "=" * 70)
    print("Demo voltooid! De tool is klaar voor gebruik.")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()

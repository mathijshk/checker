"""
Report Generator

Module voor het genereren van rapporten voor directie en bestuur.
"""

from datetime import datetime
import os
import re

class ReportGenerator:
    """Genereert rapporten voor directiesessies."""

    def __init__(self):
        self.report_types = [
            "executive_summary",
            "detailed_assessment",
            "compliance_report",
            "action_plan"
        ]

    def generate_executive_summary(self, assessment_data, compliance_data):
        """Genereer een managementsamenvatting voor directie en bestuur."""
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

        report = f"""# AI Governance Rapport voor Directie en Bestuur

**Datum:** {timestamp}
**Gegenereerd door:** AI Governance Checker

---

## Management Samenvatting

Dit rapport geeft een overzicht van de AI-gereedheid, compliance status en governance volwassenheid van uw organisatie.

"""

        # Assessment sectie
        if assessment_data:
            report += "## 1. AI Readiness Assessment\n\n"
            report += "### Scores per Categorie\n\n"

            total_score = sum(assessment_data.values()) / len(assessment_data)

            for category, score in assessment_data.items():
                status = "✓" if score >= 3.5 else "⚠" if score >= 2.5 else "✗"
                report += f"- **{category}**: {score:.1f}/5.0 {status}\n"

            report += f"\n**Overall Readiness Score:** {total_score:.1f}/5.0\n\n"

            if total_score >= 4.0:
                assessment_conclusion = "Uw organisatie heeft een **sterke AI readiness**. Blijf investeren in deze gebieden."
            elif total_score >= 3.0:
                assessment_conclusion = "Uw organisatie heeft een **goede basis** voor AI. Verbeter de zwakkere gebieden."
            elif total_score >= 2.0:
                assessment_conclusion = "Uw organisatie is **ontwikkelend** op AI gebied. Gerichte investeringen nodig."
            else:
                assessment_conclusion = "Uw organisatie heeft **beperkte AI readiness**. Urgente actie vereist."

            report += f"**Conclusie:** {assessment_conclusion}\n\n"

        # Compliance sectie
        if compliance_data:
            report += "## 2. EU AI Act Compliance\n\n"

            if 'forbidden' in compliance_data and compliance_data['forbidden']:
                report += "### ⚠ WAARSCHUWING: Verboden AI-systeem\n\n"
                report += f"Het geanalyseerde systeem '{compliance_data['system_name']}' valt onder **verboden AI-toepassingen** volgens de EU AI Act.\n\n"
                report += "**Aanbeveling:** Stop het gebruik van dit systeem onmiddellijk en consulteer juridisch advies.\n\n"
            else:
                report += f"**Systeem:** {compliance_data.get('system_name', 'N/A')}\n"
                report += f"**Risico Niveau:** {compliance_data.get('risk_level', 'N/A')}\n"
                report += f"**Compliance Status:** {'✓ Compliant' if compliance_data.get('compliant') else '✗ Niet Compliant'}\n\n"

                if 'percentage' in compliance_data:
                    report += f"**Compliance Score:** {compliance_data['percentage']:.0f}%\n\n"

                if not compliance_data.get('compliant'):
                    report += "**Aanbeveling:** Implementeer de ontbrekende AI Act vereisten voor dit systeem.\n\n"

        # Actiepunten
        report += "## 3. Prioritaire Actiepunten voor de Directie\n\n"

        action_items = []

        if assessment_data:
            low_scores = {k: v for k, v in assessment_data.items() if v < 2.5}
            if low_scores:
                for category in low_scores:
                    action_items.append(f"Versterk **{category}** (kritiek niveau)")

        if compliance_data and not compliance_data.get('compliant'):
            action_items.append("Realiseer **AI Act compliance** voor hoog-risico systemen")

        if not action_items:
            action_items.append("Continueer huidige governance praktijken")
            action_items.append("Monitor ontwikkelingen in AI regelgeving")

        for i, item in enumerate(action_items, 1):
            report += f"{i}. {item}\n"

        # Volgende stappen
        report += "\n## 4. Aanbevolen Volgende Stappen\n\n"
        report += "1. **Korte termijn (0-3 maanden)**\n"
        report += "   - Bespreek dit rapport in de eerstvolgende directievergadering\n"
        report += "   - Wijs een AI governance verantwoordelijke aan\n"
        report += "   - Start met de hoogst geprioriteerde actiepunten\n\n"

        report += "2. **Middellange termijn (3-6 maanden)**\n"
        report += "   - Implementeer verbeterplannen voor zwakke gebieden\n"
        report += "   - Voer follow-up assessments uit\n"
        report += "   - Train management en medewerkers in AI-geletterdheid\n\n"

        report += "3. **Lange termijn (6-12 maanden)**\n"
        report += "   - Integreer AI governance in bedrijfsvoering\n"
        report += "   - Blijf compliance monitoren en updaten\n"
        report += "   - Evalueer en optimaliseer AI governance processen\n\n"

        # Disclaimer
        report += "---\n\n"
        report += "*Dit rapport is gegenereerd door AI Governance Checker en dient als hulpmiddel voor directie "
        report += "en bestuur. Voor juridisch advies of gedetailleerde compliance vereisten, consulteer een specialist.*\n"

        return report

    def format_report(self, report_data, format_type="markdown"):
        """Formatteer rapport in gewenst formaat."""
        if format_type == "markdown":
            return report_data
        elif format_type == "text":
            # Verwijder markdown formatting voor plain text
            text = report_data.replace("**", "")
            text = text.replace("# ", "")
            text = text.replace("## ", "")
            text = text.replace("### ", "")
            return text
        else:
            return report_data

    def create_action_plan(self, gaps, priorities):
        """Maak een actieplan gebaseerd op geïdentificeerde gaps."""
        action_plan = "# AI Governance Actieplan\n\n"
        action_plan += f"**Datum:** {datetime.now().strftime('%d-%m-%Y')}\n\n"

        action_plan += "## Geïdentificeerde Gaps\n\n"
        for i, gap in enumerate(gaps, 1):
            action_plan += f"{i}. {gap}\n"

        action_plan += "\n## Prioriteiten\n\n"
        for priority in priorities:
            action_plan += f"- {priority}\n"

        return action_plan

    def save_report(self, report_content, filename, output_dir="reports"):
        """Sla rapport op naar bestand.

        Args:
            report_content: De inhoud van het rapport
            filename: Gewenste bestandsnaam (zonder extensie)
            output_dir: Output directory voor rapporten (default: "reports")

        Returns:
            Het volledige pad naar het opgeslagen bestand

        Raises:
            ValueError: Als report_content leeg is of filename ongeldig is
            IOError: Als het bestand niet geschreven kan worden
        """
        # Validatie van report_content
        if not report_content or not isinstance(report_content, str):
            raise ValueError("Report content mag niet leeg zijn en moet een string zijn")

        if not report_content.strip():
            raise ValueError("Report content mag niet alleen whitespace bevatten")

        # Validatie van filename
        if not filename or not isinstance(filename, str):
            raise ValueError("Filename mag niet leeg zijn en moet een string zijn")

        # Verwijder ongeldige karakters uit filename
        safe_filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        if not safe_filename or safe_filename.strip() == '':
            raise ValueError("Filename bevat alleen ongeldige karakters")

        # Maak output directory aan als deze niet bestaat
        try:
            os.makedirs(output_dir, exist_ok=True)
        except OSError as e:
            raise IOError(f"Kan output directory '{output_dir}' niet aanmaken: {e}")

        # Genereer volledige bestandsnaam met timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_filename = os.path.join(output_dir, f"{safe_filename}_{timestamp}.md")

        # Schrijf rapport naar bestand met error handling
        try:
            with open(full_filename, 'w', encoding='utf-8') as f:
                f.write(report_content)
        except PermissionError:
            raise IOError(f"Geen schrijfrechten voor bestand '{full_filename}'")
        except OSError as e:
            raise IOError(f"Kan rapport niet opslaan: {e}")

        return full_filename

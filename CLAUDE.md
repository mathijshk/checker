# CLAUDE.md — AI Governance Checker

This file provides guidance for AI assistants (Claude and others) working in this repository.

---

## Project Overview

**AI Governance Checker** is a Dutch-language assessment platform that helps directors and board members evaluate:

- **AI readiness** (5 categories, 15 questions)
- **EU AI Act compliance** (risk classification + requirement checklist)
- **Governance maturity** (5 principles, maturity levels 1–5)
- **Executive report generation** (markdown, for board presentations)

Two interfaces are provided:
- **CLI** — interactive menu-driven (`main.py`)
- **Web app** — Flask-based questionnaire (`app.py`)

Target users: C-suite, board members, compliance officers — primarily Dutch-speaking.

---

## Repository Structure

```
checker/
├── main.py                        # CLI entry point (interactive menu)
├── app.py                         # Flask web application
├── demo.py                        # Non-interactive demo with sample data
├── requirements.txt               # Python dependencies
├── .env.example                   # Email config template
│
├── src/
│   ├── assessment/readiness.py    # AIReadinessAssessment module
│   ├── compliance/ai_act_checker.py  # AIActChecker (EU AI Act)
│   ├── governance/framework.py    # AIGovernanceFramework
│   └── reports/generator.py       # ReportGenerator
│
├── templates/                     # Flask/Jinja2 HTML templates
│   ├── index.html                 # Landing page
│   ├── assessment.html            # 16-question assessment form
│   ├── results.html               # Results display
│   └── email_results.html         # HTML email template
│
├── static/
│   └── style.css                  # 700+ line stylesheet (CSS variables, responsive)
│
├── tests/
│   └── test_report_generator.py   # Unit tests for ReportGenerator
├── test_webapp.py                 # Web app integration tests
│
└── reports/                       # Generated output (gitignored)
```

---

## Running the Application

### Web app (recommended)

```bash
pip install -r requirements.txt
cp .env.example .env          # then fill in email credentials
python app.py                 # starts Flask on http://localhost:5000
```

### CLI

```bash
python main.py                # interactive menu
python demo.py                # non-interactive demo
```

---

## Running Tests

```bash
python test_webapp.py               # 6 integration tests (module imports, routes, templates)
python -m pytest tests/             # 7 unit tests for ReportGenerator
```

All 13 tests should pass. Run both before committing changes.

---

## Dependencies

Defined in `requirements.txt`:

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.0.0 | Web framework |
| Flask-Mail | 0.9.1 | Email delivery |
| Jinja2 | 3.1.2 | Template engine |
| reportlab | 4.0.7 | PDF generation (optional) |
| markdown | 3.5.1 | Markdown processing |
| python-dotenv | 1.0.0 | Environment variable loading |

Python 3.9+ is assumed. No version is pinned for Python itself.

---

## Architecture & Key Modules

### `src/assessment/readiness.py` — `AIReadinessAssessment`

- 5 categories × 3 questions = 15-question readiness score
- Categories: Strategie, Data & Infrastructuur, Talent & Skills, Governance & Ethiek, Technologie
- Scoring: 1–5 per question; averaged per category
- Maturity levels: Kritiek / Ontwikkelend / Gevorderd / Excellent

### `src/compliance/ai_act_checker.py` — `AIActChecker`

- Keyword-based use-case risk detection
- Risk levels: UNACCEPTABLE → HIGH → LIMITED → MINIMAL
- Outputs: requirement checklist + percentage compliance score

### `src/governance/framework.py` — `AIGovernanceFramework`

- 5 principles × 3 questions = 15 questions
- Principles: Transparantie, Verantwoordelijkheid, Eerlijkheid, Privacy, Veiligheid
- Maturity levels 1–5: Initieel → Beheerd → Gedefinieerd → Kwantitatief → Optimaliseren

### `src/reports/generator.py` — `ReportGenerator`

- `generate_executive_summary()` — combines all assessment data into markdown
- `save_report()` — saves timestamped file with validation
- `create_action_plan()` — gap-based, timeline-structured action plan (0–3, 3–6, 6–12 months)

### `app.py` — Flask Web Application

Key routes:
- `GET /` — landing page
- `GET /assessment` — start questionnaire
- `POST /submit` — process answers, calculate scores, optionally send email
- `GET /results` — display results

Key functions:
- `calculate_results()` — aggregate scores per category
- `get_maturity_level()` — classify into Foundational / Responsive / Proactive / Leader
- `get_recommendations()` — priority-based recommendations
- `send_results_email()` — HTML email via Flask-Mail

---

## Conventions

### Language

All user-facing text is **Dutch**. Keep it Dutch when adding questions, labels, recommendations, or UI copy. Internal code, variable names, docstrings, and comments are English.

### Scoring

- Questions use a **1–5 Likert scale** throughout (both CLI and web).
- Web app classifies overall maturity into 4 levels; CLI/governance modules use 5 levels. Do not conflate these two systems.

### Templates

- Templates live in `templates/`. They use Jinja2.
- CSS lives exclusively in `static/style.css`. Do not add inline styles.
- Color palette is defined as CSS variables — prefer modifying variables over hardcoding values.

### Report Output

- Reports are saved to `reports/` with timestamp suffix: `rapport_YYYYMMDD_HHMMSS.md`.
- The `reports/` directory is gitignored. Do not commit generated reports.

### Environment / Secrets

- Never commit `.env`. Use `.env.example` to document required variables.
- Email credentials (`MAIL_USERNAME`, `MAIL_PASSWORD`) must come from environment, not source code.

### Error Handling

- `ReportGenerator.save_report()` has comprehensive validation (content type, filename safety, file I/O). Follow the same pattern when adding file-saving logic.
- Flask routes use session for state — do not introduce global mutable state.

---

## Testing Conventions

- Add tests to `tests/` for new module-level logic.
- Add tests to `test_webapp.py` for new Flask routes or templates.
- Tests must pass with a clean `pip install -r requirements.txt` (no extra setup).
- Mocking: use `unittest.mock` — no third-party mock libraries are used.

---

## What There Is No Support For (Yet)

- No CI/CD pipeline (no `.github/workflows`). Tests are run manually.
- No database — state is session-based (Flask sessions) or file-based (`reports/`).
- No authentication or multi-user support.
- No PDF export in web app (ReportLab is a dependency but only used in CLI flow).
- No English-language interface.

---

## Commit Style

Use concise imperative commit messages in English:

```
Add email validation to assessment form
Fix maturity level calculation for edge case scores
Update EU AI Act compliance checklist for 2025 requirements
```

---

## Git Branch Policy

Development branches follow the pattern `claude/<description>-<session-id>`. Push to your designated feature branch, never directly to `master` without an approved pull request.

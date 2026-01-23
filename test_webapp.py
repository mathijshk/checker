"""
Test script for AI Governance Assessment Web App
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing imports...")
    try:
        import flask
        print("✓ Flask imported successfully")

        import flask_mail
        print("✓ Flask-Mail imported successfully")

        from app import app, ASSESSMENT_QUESTIONS
        print("✓ App module imported successfully")
        print(f"✓ Found {len(ASSESSMENT_QUESTIONS)} assessment questions")

        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("\nPlease install requirements:")
        print("  pip install -r requirements.txt")
        return False

def test_templates():
    """Test if all required templates exist."""
    print("\nTesting templates...")
    templates = [
        'templates/index.html',
        'templates/assessment.html',
        'templates/results.html',
        'templates/email_results.html'
    ]

    all_exist = True
    for template in templates:
        if os.path.exists(template):
            print(f"✓ {template} exists")
        else:
            print(f"✗ {template} NOT FOUND")
            all_exist = False

    return all_exist

def test_static_files():
    """Test if static files exist."""
    print("\nTesting static files...")
    static_files = ['static/style.css']

    all_exist = True
    for static_file in static_files:
        if os.path.exists(static_file):
            print(f"✓ {static_file} exists")
        else:
            print(f"✗ {static_file} NOT FOUND")
            all_exist = False

    return all_exist

def test_environment():
    """Test environment configuration."""
    print("\nTesting environment...")

    if os.path.exists('.env'):
        print("✓ .env file found")
        print("  Make sure to configure email settings!")
    else:
        print("⚠ .env file not found")
        print("  Copy .env.example to .env and configure email settings")

    if os.path.exists('.env.example'):
        print("✓ .env.example file exists")
    else:
        print("✗ .env.example NOT FOUND")

    return True

def test_app_routes():
    """Test if Flask app has required routes."""
    print("\nTesting Flask routes...")
    try:
        from app import app

        routes = []
        for rule in app.url_map.iter_rules():
            routes.append(str(rule))

        required_routes = ['/', '/assessment', '/submit', '/results']

        all_exist = True
        for route in required_routes:
            if route in routes:
                print(f"✓ Route {route} exists")
            else:
                print(f"✗ Route {route} NOT FOUND")
                all_exist = False

        return all_exist
    except Exception as e:
        print(f"✗ Error testing routes: {e}")
        return False

def test_assessment_questions():
    """Validate assessment questions structure."""
    print("\nValidating assessment questions...")
    try:
        from app import ASSESSMENT_QUESTIONS

        issues = []

        # Check we have at least 15 questions
        if len(ASSESSMENT_QUESTIONS) < 15:
            issues.append(f"Only {len(ASSESSMENT_QUESTIONS)} questions (expected at least 15)")
        else:
            print(f"✓ {len(ASSESSMENT_QUESTIONS)} questions found (meets 15+ requirement)")

        # Validate each question structure
        for i, q in enumerate(ASSESSMENT_QUESTIONS, 1):
            if 'id' not in q:
                issues.append(f"Question {i}: missing 'id'")
            if 'category' not in q:
                issues.append(f"Question {i}: missing 'category'")
            if 'question' not in q:
                issues.append(f"Question {i}: missing 'question'")
            if 'options' not in q:
                issues.append(f"Question {i}: missing 'options'")
            elif len(q['options']) < 2:
                issues.append(f"Question {i}: needs at least 2 options")

        if issues:
            print("✗ Issues found:")
            for issue in issues:
                print(f"  - {issue}")
            return False
        else:
            print("✓ All questions have valid structure")

            # Show categories
            categories = set(q['category'] for q in ASSESSMENT_QUESTIONS)
            print(f"✓ Categories covered: {', '.join(sorted(categories))}")

            return True

    except Exception as e:
        print(f"✗ Error validating questions: {e}")
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("AI Governance Assessment Web App - Test Suite")
    print("=" * 60)

    tests = [
        test_imports,
        test_templates,
        test_static_files,
        test_environment,
        test_app_routes,
        test_assessment_questions
    ]

    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            results.append(False)

    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    passed = sum(results)
    total = len(results)

    if passed == total:
        print(f"✓ ALL TESTS PASSED ({passed}/{total})")
        print("\nYour web app is ready to run!")
        print("\nTo start the application:")
        print("  1. Configure .env file with email settings")
        print("  2. Run: python app.py")
        print("  3. Open: http://localhost:5000")
        return 0
    else:
        print(f"✗ SOME TESTS FAILED ({passed}/{total} passed)")
        print("\nPlease fix the issues above before running the app.")
        return 1

if __name__ == '__main__':
    sys.exit(main())

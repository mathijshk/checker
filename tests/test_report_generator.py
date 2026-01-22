"""
Unit tests voor ReportGenerator

Test de error handling en validation van de report generator.
"""

import unittest
import os
import shutil
import sys

# Voeg parent directory toe aan path voor imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.reports.generator import ReportGenerator


class TestReportGenerator(unittest.TestCase):
    """Test cases voor ReportGenerator class."""

    def setUp(self):
        """Setup voor elke test."""
        self.generator = ReportGenerator()
        self.test_output_dir = "test_reports"

    def tearDown(self):
        """Cleanup na elke test."""
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)

    def test_save_report_success(self):
        """Test succesvolle rapportopslag."""
        content = "# Test Rapport\n\nDit is een test rapport."
        filename = "test_report"

        result = self.generator.save_report(content, filename, self.test_output_dir)

        self.assertTrue(os.path.exists(result))
        self.assertIn("test_report", result)
        self.assertTrue(result.endswith(".md"))

        # Verificeer inhoud
        with open(result, 'r', encoding='utf-8') as f:
            saved_content = f.read()
        self.assertEqual(saved_content, content)

    def test_save_report_empty_content_raises_error(self):
        """Test dat lege content een ValueError geeft."""
        with self.assertRaises(ValueError) as context:
            self.generator.save_report("", "test", self.test_output_dir)
        self.assertIn("leeg", str(context.exception).lower())

    def test_save_report_whitespace_only_content_raises_error(self):
        """Test dat alleen whitespace een ValueError geeft."""
        with self.assertRaises(ValueError) as context:
            self.generator.save_report("   \n  \t  ", "test", self.test_output_dir)
        self.assertIn("whitespace", str(context.exception).lower())

    def test_save_report_none_content_raises_error(self):
        """Test dat None content een ValueError geeft."""
        with self.assertRaises(ValueError) as context:
            self.generator.save_report(None, "test", self.test_output_dir)
        self.assertIn("string", str(context.exception).lower())

    def test_save_report_empty_filename_raises_error(self):
        """Test dat lege filename een ValueError geeft."""
        with self.assertRaises(ValueError) as context:
            self.generator.save_report("content", "", self.test_output_dir)
        self.assertIn("leeg", str(context.exception).lower())

    def test_save_report_invalid_filename_characters(self):
        """Test dat ongeldige karakters in filename worden vervangen."""
        content = "# Test\n\nContent"
        filename = "test<>report:file"

        result = self.generator.save_report(content, filename, self.test_output_dir)

        self.assertTrue(os.path.exists(result))
        # Ongeldige karakters moeten vervangen zijn door underscores
        self.assertNotIn("<", result)
        self.assertNotIn(">", result)
        self.assertNotIn(":", result)

    def test_save_report_creates_directory(self):
        """Test dat output directory wordt aangemaakt als deze niet bestaat."""
        content = "# Test\n\nContent"
        filename = "test"

        self.assertFalse(os.path.exists(self.test_output_dir))

        result = self.generator.save_report(content, filename, self.test_output_dir)

        self.assertTrue(os.path.exists(self.test_output_dir))
        self.assertTrue(os.path.exists(result))


if __name__ == '__main__':
    unittest.main()

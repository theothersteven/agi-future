"""Reading-list regression checks. Run with `python3 -m unittest`."""

import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

import build
import content


class ReadingTests(unittest.TestCase):
    def test_authors_follow_link_in_same_grid_cell(self):
        row = ET.fromstring(build.render_reading("ai_productivity"))
        self.assertEqual(len(row), 2)
        self.assertEqual(row[0].get("class"), "refdate")
        self.assertEqual(row[0].text, "Aug 2026")
        details = row[1]
        self.assertEqual(details.get("class"), "refdetails")
        self.assertEqual([child.tag for child in details], ["a", "span"])
        self.assertEqual(details[0].text, "Understanding AI and Productivity")
        self.assertEqual(details[0].get("href"), content.READINGS["ai_productivity"]["url"])
        self.assertEqual(details[1].get("class"), "byline")
        self.assertEqual(details[1].text, "— Chad Syverson")

    def test_every_reading_has_authors_and_keeps_chronological_order(self):
        rows = ET.fromstring("<ol>" + build.render_bibliography() + "</ol>")
        expected = sorted(content.READINGS.values(), key=lambda r: (r["date"], r["title"]))
        self.assertEqual(len(rows), len(expected))
        for row, reading in zip(rows, expected):
            with self.subTest(title=reading["title"]):
                self.assertEqual(row[0].text, build.pretty_date(reading["date"]))
                self.assertEqual(row[1][0].get("href"), reading["url"])
                self.assertEqual(row[1][0].text, reading["title"])
                self.assertTrue(reading["authors"])
                self.assertEqual(row[1][1].text, "— " + reading["authors"])

    def test_reading_fields_are_html_escaped(self):
        reading = {
            "date": "2026-08",
            "title": 'A < B & "C"',
            "url": "https://example.com/?a=1&b=2",
            "authors": 'A & B <script>"C"</script>',
        }
        with patch.dict(content.READINGS, {"test": reading}):
            rendered = build.render_reading("test")
        self.assertNotIn("<script>", rendered)
        row = ET.fromstring(rendered)
        self.assertEqual(row[1][0].text, reading["title"])
        self.assertEqual(row[1][0].get("href"), reading["url"])
        self.assertEqual(row[1][1].text, "— " + reading["authors"])

    def test_missing_author_does_not_leave_empty_byline(self):
        reading = {"date": "2026-08", "title": "Example", "url": "https://example.com"}
        for authors in (None, ""):
            with self.subTest(authors=authors):
                if authors is not None:
                    reading["authors"] = authors
                with patch.dict(content.READINGS, {"test": reading}):
                    rendered = build.render_reading("test")
                self.assertNotIn("byline", rendered)
                self.assertNotIn("—", rendered)
                self.assertEqual(len(ET.fromstring(rendered)[1]), 1)


if __name__ == "__main__":
    unittest.main()

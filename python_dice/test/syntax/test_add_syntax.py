import re
from unittest import TestCase

from python_dice.src.syntax.add_syntax import AddSyntax


class TestAddSyntax(TestCase):
    def test_add_get_token_name(self):
        self.assertEqual("ADD", AddSyntax.get_token_name())

    def test_add_get_token_regex(self):
        self.assertEqual(r"\+", AddSyntax.get_token_regex())

    def test_add_regex_will_match(self):
        test_cases = ["+"]
        for test_case in test_cases:
            self.assertTrue(
                re.match(AddSyntax.get_token_regex(), test_case),
                "did not match on case test_case %s" % test_case,
            )

    def test_add_regex_will_not_match(self):
        test_cases = ["a", "just a string", "", "1", " ", "-", "*", "("]
        for test_case in test_cases:
            self.assertIsNone(
                re.match(AddSyntax.get_token_regex(), test_case),
                "matched on case test_case %s" % test_case,
            )

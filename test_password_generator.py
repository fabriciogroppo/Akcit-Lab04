# -*- coding: utf-8 -*-

import unittest
import string

from password_generator import generate_password


class PasswordGeneratorTests(unittest.TestCase):
    def test_length_is_respected(self):
        password = generate_password(length=24)
        self.assertEqual(len(password), 24)

    def test_requires_at_least_one_character_set(self):
        with self.assertRaises(ValueError):
            generate_password(length=12, use_digits=False, use_lower=False, use_upper=False, use_symbols=False)

    def test_generated_password_contains_selected_categories(self):
        password = generate_password(length=12, use_digits=True, use_lower=True, use_upper=True, use_symbols=False)
        self.assertTrue(any(ch in string.digits for ch in password))
        self.assertTrue(any(ch in string.ascii_lowercase for ch in password))
        self.assertTrue(any(ch in string.ascii_uppercase for ch in password))

    def test_password_randomness_quick_check(self):
        first = generate_password(length=16, use_digits=True, use_lower=True, use_upper=True, use_symbols=False)
        second = generate_password(length=16, use_digits=True, use_lower=True, use_upper=True, use_symbols=False)
        self.assertNotEqual(first, second)

    def test_length_one_password(self):
        password = generate_password(length=1, use_digits=True, use_lower=False, use_upper=False, use_symbols=False)
        self.assertEqual(len(password), 1)


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

import os
import unittest
import string

from config.settings import Settings
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

    def test_settings_reads_env_file(self):
        env_path = os.path.join(os.path.dirname(__file__), '.env.test')
        with open(env_path, 'w') as env_file:
            env_file.write('PASSWORD_LENGTH=8\n')
            env_file.write('USE_DIGITS=False\n')
            env_file.write('USE_LOWER=False\n')
            env_file.write('USE_UPPER=True\n')
            env_file.write('USE_SYMBOLS=True\n')

        settings = Settings(env_path=env_path)
        self.assertEqual(settings.length, 8)
        self.assertFalse(settings.use_digits)
        self.assertFalse(settings.use_lower)
        self.assertTrue(settings.use_upper)
        self.assertTrue(settings.use_symbols)

        os.remove(env_path)


if __name__ == '__main__':
    unittest.main()

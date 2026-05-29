#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Settings(object):
    DEFAULT_LENGTH = 16
    DEFAULT_USE_DIGITS = True
    DEFAULT_USE_LOWER = True
    DEFAULT_USE_UPPER = True
    DEFAULT_USE_SYMBOLS = False

    def __init__(self, env_path=None):
        self.length = self.DEFAULT_LENGTH
        self.use_digits = self.DEFAULT_USE_DIGITS
        self.use_lower = self.DEFAULT_USE_LOWER
        self.use_upper = self.DEFAULT_USE_UPPER
        self.use_symbols = self.DEFAULT_USE_SYMBOLS

        if env_path is None:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            env_path = os.path.join(base_dir, '.env')

        self._load_env(env_path)

    def _load_env(self, env_path):
        try:
            with open(env_path, 'r') as env_file:
                for line in env_file:
                    raw_line = line.strip()
                    if not raw_line or raw_line.startswith('#'):
                        continue
                    if '=' not in raw_line:
                        continue
                    name, value = raw_line.split('=', 1)
                    self._set_option(name.strip(), value.strip())
        except IOError:
            pass

    def _set_option(self, name, value):
        name = name.upper()
        if name == 'PASSWORD_LENGTH':
            self.length = self._parse_int(value, self.DEFAULT_LENGTH)
        elif name == 'USE_DIGITS':
            self.use_digits = self._parse_bool(value, self.DEFAULT_USE_DIGITS)
        elif name == 'USE_LOWER':
            self.use_lower = self._parse_bool(value, self.DEFAULT_USE_LOWER)
        elif name == 'USE_UPPER':
            self.use_upper = self._parse_bool(value, self.DEFAULT_USE_UPPER)
        elif name == 'USE_SYMBOLS':
            self.use_symbols = self._parse_bool(value, self.DEFAULT_USE_SYMBOLS)

    def _parse_int(self, value, default):
        try:
            return int(value)
        except ValueError:
            return default

    def _parse_bool(self, value, default):
        value = value.lower()
        if value in ('1', 'true', 'yes', 'on'):
            return True
        if value in ('0', 'false', 'no', 'off'):
            return False
        return default

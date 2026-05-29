#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

from config.settings import Settings
from services.password_service import generate_password


def parse_cli_args(settings):
    parser = argparse.ArgumentParser(description='Generate a secure random password.')
    parser.add_argument('-l', '--length', type=int, default=settings.length,
                        help='Password length (default: %s)' % settings.length)
    parser.add_argument('-n', '--no-digits', action='store_true', default=not settings.use_digits,
                        help='Exclude digits from the password')
    parser.add_argument('-L', '--no-lower', action='store_true', default=not settings.use_lower,
                        help='Exclude lowercase letters from the password')
    parser.add_argument('-U', '--no-upper', action='store_true', default=not settings.use_upper,
                        help='Exclude uppercase letters from the password')
    parser.add_argument('-s', '--symbols', action='store_true', default=settings.use_symbols,
                        help='Include punctuation symbols in the password')
    return parser.parse_args()


def main():
    settings = Settings()
    args = parse_cli_args(settings)

    try:
        password = generate_password(
            length=args.length,
            use_digits=not args.no_digits,
            use_lower=not args.no_lower,
            use_upper=not args.no_upper,
            use_symbols=args.symbols,
        )
    except ValueError as exc:
        sys.stderr.write('Error: %s\n' % exc)
        sys.exit(1)

    sys.stdout.write(password + '\n')


if __name__ == '__main__':
    main()

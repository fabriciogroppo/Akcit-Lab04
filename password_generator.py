#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random
import string
import sys


def generate_password(length=16, use_digits=True, use_lower=True, use_upper=True, use_symbols=False):
    """Generate a random password according to user-defined criteria."""
    if length < 1:
        raise ValueError("Password length must be at least 1")

    pools = []
    if use_digits:
        pools.append(string.digits)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("At least one character set must be enabled")

    secure_random = random.SystemRandom()
    all_characters = ''.join(pools)
    password = []

    # Guarantee that at least one character from each selected category is included
    for pool in pools:
        password.append(secure_random.choice(pool))

    remaining = length - len(password)
    for _ in range(remaining):
        password.append(secure_random.choice(all_characters))

    secure_random.shuffle(password)
    return ''.join(password)


def parse_cli_args():
    parser = argparse.ArgumentParser(description='Generate a secure random password.')
    parser.add_argument('-l', '--length', type=int, default=16,
                        help='Password length (default: 16)')
    parser.add_argument('-n', '--no-digits', action='store_true',
                        help='Exclude digits from the password')
    parser.add_argument('-L', '--no-lower', action='store_true',
                        help='Exclude lowercase letters from the password')
    parser.add_argument('-U', '--no-upper', action='store_true',
                        help='Exclude uppercase letters from the password')
    parser.add_argument('-s', '--symbols', action='store_true',
                        help='Include punctuation symbols in the password')
    return parser.parse_args()


def main():
    args = parse_cli_args()
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

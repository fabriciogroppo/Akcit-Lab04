#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string


def generate_password(length=16, use_digits=True, use_lower=True, use_upper=True, use_symbols=False):
    if length < 1:
        raise ValueError('Password length must be at least 1')

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
        raise ValueError('At least one character set must be enabled')

    secure_random = random.SystemRandom()
    all_characters = ''.join(pools)
    password = []

    for pool in pools:
        password.append(secure_random.choice(pool))

    for _ in range(length - len(password)):
        password.append(secure_random.choice(all_characters))

    secure_random.shuffle(password)
    return ''.join(password)

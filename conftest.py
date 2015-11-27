# -*- coding: utf-8 -*-
"""
    confest.py
    ~~~~~~~~~~

    set up fixtures for solution tests
"""

import pytest


@pytest.fixture(scope='session')
def deck3x4():
    return [
        [3, 1, 1], [2, 0, 3], [0, 2, 0],
        [1, 3, 2], [0, 1, 0], [2, 1, 2], [1, 1, 3]
    ]


@pytest.fixture(scope='session')
def deck4x5():
    return [
        [3, 2, 1, 2], [0, 0, 3, 3], [2, 3, 2, 1],
        [4, 1, 4, 0], [1, 4, 0, 4], [2, 2, 3, 0]
    ]

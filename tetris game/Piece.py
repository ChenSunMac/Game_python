# -*- coding: utf-8 -*-
"""
Class Piece:
    The shapes of tetrimonos

    each of them was a tuple of tuples containing the rotations
    
    PIECES is a dict containing all the shapes where number as a key.

    {1: I, 2: J, 3: L, 4: O, 5: S, 6:T, 7:Z}

@author: Chens
https://github.com/ChenSunMac
"""

class Piece:
    # I
    I = (
            (
                (0, 0, 0, 0),
                (1, 1, 1, 1),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 0, 1, 0),
                (0, 0, 1, 0),
                (0, 0, 1, 0),
                (0, 0, 1, 0)
            ),
            (
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (1, 1, 1, 1),
                (0, 0, 0, 0)
            ),
            (
                (0, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 1, 0, 0),
                (0, 1, 0, 0)
            )
        )
    # J
    J = (
            (
                (2, 0, 0, 0),
                (2, 2, 2, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 2, 2, 0),
                (0, 2, 0, 0),
                (0, 2, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 0, 0, 0),
                (2, 2, 2, 0),
                (0, 0, 2, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 2, 0, 0),
                (0, 2, 0, 0),
                (2, 2, 0, 0),
                (0, 0, 0, 0)
            )
        )
    # L
    L = (
            (
                (0, 0, 3, 0),
                (3, 3, 3, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 3, 0, 0),
                (0, 3, 0, 0),
                (0, 3, 3, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 0, 0, 0),
                (3, 3, 3, 0),
                (3, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (3, 3, 0, 0),
                (0, 3, 0, 0),
                (0, 3, 0, 0),
                (0, 0, 0, 0)
            )
        )
    # O
    O = (
            (
                (0, 4, 4, 0),
                (0, 4, 4, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 4, 4, 0),
                (0, 4, 4, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 4, 4, 0),
                (0, 4, 4, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 4, 4, 0),
                (0, 4, 4, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            )
        )
    # S
    S = (
            (
                (0, 5, 5, 0),
                (5, 5, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 5, 0, 0),
                (0, 5, 5, 0),
                (0, 0, 5, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 0, 0, 0),
                (0, 5, 5, 0),
                (5, 5, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (5, 0, 0, 0),
                (5, 5, 0, 0),
                (0, 5, 0, 0),
                (0, 0, 0, 0)
            )
        )
    # T
    T = (
            (
                (0, 6, 0, 0),
                (6, 6, 6, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 6, 0, 0),
                (0, 6, 6, 0),
                (0, 6, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 0, 0, 0),
                (6, 6, 6, 0),
                (0, 6, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 6, 0, 0),
                (6, 6, 0, 0),
                (0, 6, 0, 0),
                (0, 0, 0, 0)
            )
        )
    # Z
    Z = (
            (
                (7, 7, 0, 0),
                (0, 7, 7, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 0, 7, 0),
                (0, 7, 7, 0),
                (0, 7, 0, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 0, 0, 0),
                (7, 7, 0, 0),
                (0, 7, 7, 0),
                (0, 0, 0, 0)
            ),
            (
                (0, 7, 0, 0),
                (7, 7, 0, 0),
                (7, 0, 0, 0),
                (0, 0, 0, 0)
            )
        )

    PIECES = {1: I, 2: J, 3: L, 4: O, 5: S, 6:T, 7:Z}
    TETRIMINO_SIZE = 4
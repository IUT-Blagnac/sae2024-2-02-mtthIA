from itertools import groupby, batched
# ATTENTION : Nécessite Python >= 3.12 pour itertools.batched


def n_chars(c: str, n: int) -> str:
    """
    Encodage RLE pour un caractère et un nombre. Gère les cas à 9 ou plus.

    >>> n_chars('z', 5)
    '5z'
    >>> n_chars('W', 11)
    '9W2W'
    """
    res = []
    while n > 9:
        res.append(f'9{c}')
        n -= 9
    res.append(f'{n}{c}')
    return ''.join(res)


def rle(s: str) -> str:
    """
    Compression RLE.

    >>> rle('abbccc')
    '1a2b3c'
    """
    return ''.join(n_chars(char, len(list(items)))
                   for char, items in groupby(s))  # groupe par lettres identiques


def unrle(s: str) -> str:
    """
    Décompression RLE.

    >>> unrle('1a2b3c')
    'abbccc'
    """
    return ''.join(char * int(n)
                   for n, char in batched(s, 2))  # groupe par 2


print(unrle("2d5e2d5e"))
print(unrle(""))
print(unrle("aaaff"))
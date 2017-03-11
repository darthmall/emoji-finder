import re


EMOJI = re.compile(u"(?:(?:[\ud83c-\ud83e][\udc00-\udfff])|[\u00a0-\u329f])(?:\ud83c[\udffb-\udfff]|[\ufe0e-\ufe0f])?")


def surrogate_pairs(code_point):
    """Return the UTF-16 high and low surrogates for a unicode code point.

    Arguments:
    code_point -- A string representation of the form 'U+xxxxx' or
                     '\Uxxxxxxxx'

    Returns:
    A tuple containing the surrogate pairs as hexadecimal strings:
    (high, low), or (code_point,) if the code point is in the Basic
    Multilingual Plane.
    """
    # Strip the first two characters, assuming either "\U" or "U+"
    # prefixes on the code point.
    ordinal = int(code_point[2:], 16)

    if ordinal <= 0xd7ff or (ordinal >= 0xe000 and ordinal <= 0xffff):
        # Code points in the range U+0000-U+D7FF and U+E000-U+FFFF
        # need no conversion.
        return (hex(ordinal), )

    bits = bin(ordinal - 0x10000)[2:].zfill(20)
    low = int(bits[10:], 2) + 0xdc00
    high = int(bits[:10], 2) + 0xd800

    return (hex(high), hex(low))


def extract(s):
    return EMOJI.findall(s)


if __name__ == "__main__":
    import sys

    for code_point in sys.argv[1:]:
        print surrogate_pairs(code_point)

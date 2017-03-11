import re

# Regex for matching emoji and other symbols: first line catches all
# symbols in the Basic Multilingual Plane (BMP), second line catches
# emoji and symbols in Supplementary Planes, third line includes
# subsequent characters that modify emoji: i.e. text or emoji variant
# and skin tones, so that those characters are kept with the characters
# they affect when tokenizing.
EMOJI = re.compile(u"(?:[\u00a0-\u329f]"
                   u"|[\ud83c-\ud83e][\udc00-\udfff])"
                   u"(?:[\ufe0e-\ufe0f]|\ud83c[\udffb-\udfff])?")


def surrogate_pairs(code_point):
    """Return the UTF-16 high and low surrogates for a unicode code point.

    Arguments:
    code_point -- A string representation of the form 'U+xxxxx' or '\Uxxxxxxxx'

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
    """Return a list of each individual emoji in the string."""
    return EMOJI.findall(s)


def test(s):
    """Return true if the string contains any emoji."""
    return EMOJI.search(s) is not None


if __name__ == "__main__":
    import sys

    for code_point in sys.argv[1:]:
        print surrogate_pairs(code_point)

import regex as re


EMOJI = re.compile(u".*", re.UNICODE)


def surrogate_pairs(codepoint):
    ordinal = int(codepoint[2:], 16)

    if ordinal <= 0xd7ff or (ordinal >= 0xe000 and ordinal <= 0xffff):
        return (hex(ordinal), )

    bits = bin(ordinal - 0x10000)[2:].zfill(20)
    low = int(bits[10:], 2) + 0xdc00
    high = int(bits[:10], 2) + 0xd800

    return (hex(high), hex(low))


def extract(s):
    return EMOJI.findall(s)


if __name__ == "__main__":
    import sys

    print surrogate_pairs(sys.argv[1])

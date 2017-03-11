# coding: utf-8
import unittest

import emoji


class TestEmoji(unittest.TestCase):
    def test_surrogate_pairs(self):
        self.assertEqual(emoji.surrogate_pairs("U+10437"),
                         ("0xd801", "0xdc37"))
        self.assertEqual(emoji.surrogate_pairs("\U00010437"),
                         ("0xd801", "0xdc37"))
        self.assertEqual(emoji.surrogate_pairs("U+20AC"), ("0x20ac",))

    def test_extract(self):
        self.assertEqual(emoji.extract(u"Hello, 😂. 🤡"), [u"😂", u"🤡"])


if __name__ == "__main__":
    unittest.main()

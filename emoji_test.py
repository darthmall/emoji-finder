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

    def test_extract_non_emoji(self):
        self.assertEqual(emoji.extract(u"\U0001efff"), [])

    def test_extract_variant_forms(self):
        self.assertEqual(emoji.extract(u"\u2600"), [u"\u2600"])
        self.assertEqual(emoji.extract(u"\u2600\ufe0f"), [u"\u2600\ufe0f"])
        self.assertEqual(emoji.extract(u"\u2600\ufe0e"), [u"\u2600\ufe0e"])
        self.assertNotEqual(emoji.extract(u"\2600\ufe0f"), [u"\u2600"])

    def test_extract_skin_tones(self):
        self.assertEqual(emoji.extract(u"👂"), [u"\U0001f442"])
        self.assertEqual(emoji.extract(u"👂🏾"), [u"\U0001f442\U0001f3fe"])
        self.assertEqual(emoji.extract(u"👂👂🏾👂👂🏿"),
                         [u"\U0001f442", u"\U0001f442\U0001f3fe",
                         u"\U0001f442", u"\U0001f442\U0001f3ff"])

    def test_extract(self):
        self.assertEqual(emoji.extract(u"🀄️"), [u"🀄️"])

        self.assertEqual(emoji.extract(u"He🤦llo, 😂. 🤡"),
                         [u"🤦", u"😂", u"🤡"])

    def test_test(self):
        self.assertTrue(emoji.test("hello 🇯🇵"))
        self.assertFalse(emoji.test("hello japan"))


if __name__ == "__main__":
    unittest.main()

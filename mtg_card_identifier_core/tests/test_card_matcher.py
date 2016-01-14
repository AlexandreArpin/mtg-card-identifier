from django.test import TestCase

from mtg_card_identifier_core.mtg_card_matcher import match_card


class InvalidInputMatcherTest(TestCase):

    def test_all_none(self):
        result = match_card()

        self.assertIsNone(result)


class ExactMatcherTest(TestCase):

    def test_exact_avacyn_guardian_angel(self):
        result = match_card("Avacyn, Guardian Angel", "003", edition="m15")

        self.assertEquals("Avacyn, Guardian Angel", result["name"])
        self.assertEquals("3", result["number"])

    def test_exact_ainok_bond_kin(self):
        result = match_card("Ainok Bond-Kin", "003", edition="ktk")

        self.assertEquals("Ainok Bond-Kin", result["name"])
        self.assertEquals("3", result["number"])


class ExactCardNameMatcherTest(TestCase):

    def test_exact_name_dtk_champion_of_arashin(self):
        result = match_card("Champion of Arashin", edition="dtk")

        self.assertEquals("Champion of Arashin", result["name"])
        self.assertEquals("9", result["number"])

    def test_exact_name_bfz_endless_one(self):
        result = match_card("Endless One", edition="bfz")

        self.assertEquals("Endless One", result["name"])
        self.assertEquals("8", result["number"])

    def test_exact_name_bfz_tandem_tactics(self):
        result = match_card("Tandem Tactics", edition="bfz")

        self.assertEquals("Tandem Tactics", result["name"])
        self.assertEquals("52", result["number"])


class ExactCardNumberMatcherTest(TestCase):

    def test_exact_number_dtk_champion_of_arashin(self):
        result = match_card(None, 9, edition="dtk")

        self.assertEquals("Champion of Arashin", result["name"])
        self.assertEquals("9", result["number"])

    def test_exact_number_bfz_endless_one(self):
        result = match_card(None, 8, edition="bfz")

        self.assertEquals("Endless One", result["name"])
        self.assertEquals("8", result["number"])

    def test_exact_number_bfz_tandem_tactics(self):
        result = match_card(None, 52, edition="bfz")

        self.assertEquals("Tandem Tactics", result["name"])
        self.assertEquals("52", result["number"])

    def test_exact_number_bfz_ghostly_sentinel(self):
        result = match_card(None, "028", edition="bfz")

        self.assertEquals("Ghostly Sentinel", result["name"])
        self.assertEquals("28", result["number"])


class ExactNoEditionMatcherTest(TestCase):

    def test_exact_avacyn_guardian_angel(self):
        result = match_card("Avacyn, Guardian Angel", "003")

        self.assertEquals("Avacyn, Guardian Angel", result["name"])
        self.assertEquals("3", result["number"])
        self.assertEqual(383185, result["multiverseid"])

    def test_exact_ainok_bond_kin(self):
        result = match_card("Ainok Bond-Kin", "003")

        self.assertEquals("Ainok Bond-Kin", result["name"])
        self.assertEquals("3", result["number"])
        self.assertEqual(386471, result["multiverseid"])

    def test_exact_name_bfz_endless_one(self):
        result = match_card("Endless One")

        self.assertEquals("Endless One", result["name"])
        self.assertEquals("8", result["number"])
        self.assertEqual(401871, result["multiverseid"])


class PartialCardNameMatcherTest(TestCase):

    def test_partial_name_dtk_champion_of_arashin(self):
        result = match_card("Charnpion of Arashin", edition="dtk")

        self.assertIsNotNone(result)
        self.assertEquals("Champion of Arashin", result["name"])
        self.assertEquals("9", result["number"])

        result = match_card("Charnpion Arashin", edition="dtk")

        self.assertIsNotNone(result)
        self.assertEquals("Champion of Arashin", result["name"])
        self.assertEquals("9", result["number"])

    def test_partial_name_bfz_endless_one(self):
        result = match_card("Endless One fm", edition="bfz")

        self.assertIsNotNone(result)
        self.assertEquals("Endless One", result["name"])
        self.assertEquals("8", result["number"])

    def test_partial_name_bfz_tandem_tactics(self):
        result = match_card("Tanolem Tactios", edition="bfz")

        self.assertIsNotNone(result)
        self.assertEquals("Tandem Tactics", result["name"])
        self.assertEquals("52", result["number"])

    def test_partial_name_ori_claustrophobia(self):
        result = match_card("daListropholoia",)

        self.assertIsNotNone(result)
        self.assertEquals("Claustrophobia", result["name"])
        self.assertEquals("50", result["number"])

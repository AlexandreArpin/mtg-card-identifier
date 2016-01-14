import os

from django.test import TestCase

from mtg_card_identifier_core.opencv_card_finder import find_card_file

BASE_DIR = os.path.dirname(__file__)
NORMAL_DIR = os.path.join(BASE_DIR, "normal")
BLENDING_DIR = os.path.join(BASE_DIR, "blending_background")
ORIENTATION_DIR = os.path.join(BASE_DIR, "orientation")
PERSPECTIVE_DIR = os.path.join(BASE_DIR, "perspective")
BUSY_DIR = os.path.join(BASE_DIR, "busy_background")


class NormalCardFinderTest(TestCase):

    def test_normal_dtk_champion_of_arashin(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_champion_of_arashin.JPG")
        find_card_file(file_path)

    def test_normal_dtk_ojutais_summons(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_ojutais_summons.JPG")
        find_card_file(file_path)

    def test_normal_dtk_sarkhans_triumph(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_sarkhans_triumph.JPG")
        find_card_file(file_path)

    def test_normal_dtk_swift_warkite(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_swift_warkite.JPG")
        find_card_file(file_path)

    def test_normal_dtk_vial_of_dragonfire(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_vial_of_dragonfire.JPG")
        find_card_file(file_path)

    def test_normal_frf_reach_of_shadow(self):
        file_path = os.path.join(NORMAL_DIR, "frf_reach_of_shadow.jpg")
        find_card_file(file_path)

    def test_normal_frf_temur_battlerage(self):
        file_path = os.path.join(NORMAL_DIR, "frf_temur_battlerage.jpg")
        find_card_file(file_path)

    def test_normal_ori_forest(self):
        file_path = os.path.join(NORMAL_DIR, "ori_forest.jpg")
        find_card_file(file_path)

    def test_normal_ori_mountain(self):
        file_path = os.path.join(NORMAL_DIR, "ori_mountain.jpg")
        find_card_file(file_path)

    def test_normal_ori_swamp(self):
        file_path = os.path.join(NORMAL_DIR, "ori_swamp.jpg")
        find_card_file(file_path)


class BlendingBackgroundCardFinderTest(TestCase):

    def test_blending_dtk_lightning_berseker(self):
        file_path = os.path.join(BLENDING_DIR, "dtk_lightning_berserker.jpg")
        find_card_file(file_path)

    def test_blending_dtk_roast(self):
        file_path = os.path.join(BLENDING_DIR, "dtk_roast.jpg")
        find_card_file(file_path)

    def test_blending_frf_cunning_strike(self):
        file_path = os.path.join(BLENDING_DIR, "frf_cunning_strike.jpg")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_blending_frf_formless_nurturing(self):
        file_path = os.path.join(BLENDING_DIR, "frf_formless_nurturing.jpg")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_blending_frf_lightform(self):
        file_path = os.path.join(BLENDING_DIR, "frf_lightform.jpg")
        find_card_file(file_path)

    def test_blending_frf_tasigurs_cruelty(self):
        file_path = os.path.join(BLENDING_DIR, "frf_tasigurs_cruelty.jpg")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_blending_frf_will_of_the_naga(self):
        file_path = os.path.join(BLENDING_DIR, "frf_will_of_the_naga.jpg")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_blending_ori_blood_cursed_knight(self):
        file_path = os.path.join(BLENDING_DIR, "ori_blood_cursed_knight.jpg")
        find_card_file(file_path)

    def test_blending_ori_forest(self):
        file_path = os.path.join(BLENDING_DIR, "ori_forest.jpg")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_blending_ori_mage_ring_bully(self):
        file_path = os.path.join(BLENDING_DIR, "ori_mage_ring_bully.jpg")
        find_card_file(file_path)

    def test_blending_ori_might_of_the_masses(self):
        file_path = os.path.join(BLENDING_DIR, "ori_might_of_the_masses.JPG")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_blending_ori_mountain(self):
        file_path = os.path.join(BLENDING_DIR, "ori_mountain.jpg")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_blending_ori_swamp(self):
        file_path = os.path.join(BLENDING_DIR, "ori_swamp.jpg")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_blending_ori_tower_geist(self):
        file_path = os.path.join(BLENDING_DIR, "ori_tower_geist.JPG")
        find_card_file(file_path)

    def test_blending_ori_weight_of_the_underworld(self):
        file_path = os.path.join(BLENDING_DIR, "ori_weight_of_the_underworld.JPG")
        find_card_file(file_path)

        self.assertTrue(False)


class OrientationCardFinderTest(TestCase):

    def test_orientation_disperse_one(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_1.JPG")
        find_card_file(file_path)

    def test_orientation_disperse_two(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_2.JPG")
        find_card_file(file_path)

    def test_orientation_disperse_three(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_3.JPG")
        find_card_file(file_path)

    def test_orientation_disperse_four(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_4.JPG")
        find_card_file(file_path)

    def test_orientation_disperse_five(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_5.JPG")
        find_card_file(file_path)


class PerspectiveCardFinderTest(TestCase):

    def test_perspective_valor_in_akros_one(self):
        file_path = os.path.join(PERSPECTIVE_DIR, "ori_valor_in_akros_1.JPG")
        find_card_file(file_path)

    def test_perspective_valor_in_akros_two(self):
        file_path = os.path.join(PERSPECTIVE_DIR, "ori_valor_in_akros_2.JPG")
        find_card_file(file_path)

        self.assertTrue(False)


class BusyCardFinderTest(TestCase):

    def test_busy_scour_from_existence_one(self):
        file_path = os.path.join(BUSY_DIR, "bfz_scour_from_existence_1.JPG")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_busy_scour_from_existence_two(self):
        file_path = os.path.join(BUSY_DIR, "bfz_scour_from_existence_2.JPG")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_busy_scour_from_existence_three(self):
        file_path = os.path.join(BUSY_DIR, "bfz_scour_from_existence_3.JPG")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_busy_bfz_stone_haven_medic_one(self):
        file_path = os.path.join(BUSY_DIR, "bfz_stone_haven_medic_1.JPG")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_busy_bfz_stone_haven_medic_two(self):
        file_path = os.path.join(BUSY_DIR, "bfz_stone_haven_medic_2.JPG")
        find_card_file(file_path)

    def test_busy_bfz_stone_haven_medic_three(self):
        file_path = os.path.join(BUSY_DIR, "bfz_stone_haven_medic_3.JPG")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_busy_bfz_stone_haven_medic_four(self):
        file_path = os.path.join(BUSY_DIR, "bfz_stone_haven_medic_4.JPG")
        find_card_file(file_path)

    def test_busy_dtk_gurmag_drowner_one(self):
        file_path = os.path.join(BUSY_DIR, "dtk_gurmag_drowner_1.JPG")
        find_card_file(file_path)

    def test_busy_dtk_gurmag_drowner_two(self):
        file_path = os.path.join(BUSY_DIR, "dtk_gurmag_drowner_2.JPG")
        find_card_file(file_path)

        self.assertTrue(False)

    def test_busy_dtk_gurmag_drowner_three(self):
        file_path = os.path.join(BUSY_DIR, "dtk_gurmag_drowner_3.JPG")
        find_card_file(file_path)

        self.assertTrue(False)

import os

from django.test import TestCase
from mtg_card_identifier_core.opencv_mtg_identifier import identify_file

BASE_DIR = os.path.dirname(__file__)
GATHERER_DIR = os.path.join(BASE_DIR, "gatherer")
MAGIC_CARD_INFO_DIR = os.path.join(BASE_DIR, "magiccardinfo")
NORMAL_DIR = os.path.join(BASE_DIR, "normal")
BLENDING_DIR = os.path.join(BASE_DIR, "blending_background")
ORIENTATION_DIR = os.path.join(BASE_DIR, "orientation")
PERSPECTIVE_DIR = os.path.join(BASE_DIR, "perspective")
DAMAGED_DIR = os.path.join(BASE_DIR, "damaged")
BUSY_DIR = os.path.join(BASE_DIR, "busy_background")


class GathererCardIdentifierTest(TestCase):

    def test_gatherer_dtk_vial_of_dragonfire(self):
        file_path = os.path.join(GATHERER_DIR, "dtk_vial_of_dragonfire.jpg")
        card = identify_file(file_path)

        self.assertEqual("Vial of Dragonfire", card["name"])

    def test_gatherer_frf_cunning_strike(self):
        file_path = os.path.join(GATHERER_DIR, "frf_cunning_strike.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Cunning Strike", card["name"])

    def test_gatherer_frf_reach_of_shadow(self):
        file_path = os.path.join(GATHERER_DIR, "frf_reach_of_shadow.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Reach of Shadows", card["name"])

    def test_gatherer_frf_torrent_elemental(self):
        file_path = os.path.join(GATHERER_DIR, "frf_torrent_elemental.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Torrent Elemental", card["name"])

    def test_gatherer_frf_ugin_the_spirit_dragon(self):
        file_path = os.path.join(GATHERER_DIR, "frf_ugin_the_spirit_dragon.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Ugin, the Spirit Dragon", card["name"])

    def test_gatherer_ktk_mountain(self):
        file_path = os.path.join(GATHERER_DIR, "ktk_mountain.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Mountain", card["name"])

    def test_gatherer_m15_swamp(self):
        file_path = os.path.join(GATHERER_DIR, "m15_swamp.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Swamp", card["name"])

    def test_gatherer_ori_thornbow_archer(self):
        file_path = os.path.join(GATHERER_DIR, "ori_thornbow_archer.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Thornbow Archer", card["name"])


class MagicCardInfoCardIdentifierTest(TestCase):

    def test_magiccardinfo_dtk_vial_of_dragonfire(self):
        file_path = os.path.join(MAGIC_CARD_INFO_DIR, "dtk_vial_of_dragonfire.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Vial of Dragonfire", card["name"])

    def test_magiccardinfo_frf_cunning_strike(self):
        file_path = os.path.join(MAGIC_CARD_INFO_DIR, "frf_cunning_strike.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Cunning Strike", card["name"])

    def test_magiccardinfo_frf_reach_of_shadow(self):
        file_path = os.path.join(MAGIC_CARD_INFO_DIR, "frf_reach_of_shadow.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Reach of Shadows", card["name"])

    def test_magiccardinfo_frf_torrent_elemental(self):
        file_path = os.path.join(MAGIC_CARD_INFO_DIR, "frf_torrent_elemental.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Torrent Elemental", card["name"])

    def test_magiccardinfo_frf_ugin_the_spirit_dragon(self):
        file_path = os.path.join(MAGIC_CARD_INFO_DIR, "frf_ugin_the_spirit_dragon.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Ugin, the Spirit Dragon", card["name"])

    def test_magiccardinfo_ktk_mountain(self):
        file_path = os.path.join(MAGIC_CARD_INFO_DIR, "ktk_mountain.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Mountain", card["name"])

    def test_magiccardinfo_m15_swamp(self):
        file_path = os.path.join(MAGIC_CARD_INFO_DIR, "m15_swamp.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Swamp", card["name"])

    def test_magiccardinfo_ori_thornbow_archer(self):
        file_path = os.path.join(MAGIC_CARD_INFO_DIR, "ori_thornbow_archer.jpg")
        card = identify_file(file_path)

        self.assertIsNotNone(card)
        self.assertEqual("Thornbow Archer", card["name"])


class NormalCardIdentifierTest(TestCase):

    def test_normal_dtk_champion_of_arashin(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_champion_of_arashin.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Champion of Arashin", card["name"])

    def test_normal_dtk_ojutais_summons(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_ojutais_summons.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Ojutai's Summons", card["name"])

    def test_normal_dtk_sarkhans_triumph(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_sarkhans_triumph.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Sarkhan's Triumph", card["name"])

    def test_normal_dtk_swift_warkite(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_swift_warkite.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Swift Warkite", card["name"])

    def test_normal_dtk_vial_of_dragonfire(self):
        file_path = os.path.join(NORMAL_DIR, "dtk_vial_of_dragonfire.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Vial of Dragonfire", card["name"])

    def test_normal_frf_reach_of_shadow(self):
        file_path = os.path.join(NORMAL_DIR, "frf_reach_of_shadow.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Reach of Shadows", card["name"])

    def test_normal_frf_temur_battle_rage(self):
        file_path = os.path.join(NORMAL_DIR, "frf_temur_battlerage.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Temur Battle Rage", card["name"])

    def test_normal_ori_forest(self):
        file_path = os.path.join(NORMAL_DIR, "ori_forest.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Forest", card["name"])

    def test_normal_ori_mountain(self):
        file_path = os.path.join(NORMAL_DIR, "ori_mountain.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Mountain", card["name"])

    def test_normal_ori_swamp(self):
        file_path = os.path.join(NORMAL_DIR, "ori_swamp.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Swamp", card["name"])

    def test_normal_bfz_broodhunter_wurm(self):
        file_path = os.path.join(NORMAL_DIR, "bfz_broodhunter_wurm.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Broodhunter Wurm", card["name"])

    def test_normal_bfz_felidar_cub(self):
        file_path = os.path.join(NORMAL_DIR, "bfz_felidar_cub.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Felidar Cub", card["name"])

    def test_normal_bfz_gideons_reproach(self):
        file_path = os.path.join(NORMAL_DIR, "bfz_gideons_reproach.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Gideon's Reproach", card["name"])

    def test_normal_bfz_natural_connection(self):
        file_path = os.path.join(NORMAL_DIR, "bfz_natural_connection.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Natural Connection", card["name"])

    def test_normal_bfz_reclaiming_vines(self):
        file_path = os.path.join(NORMAL_DIR, "bfz_reclaiming_vines.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Reclaiming Vines", card["name"])

    def test_normal_bfz_sandstone_bridge(self):
        file_path = os.path.join(NORMAL_DIR, "bfz_sandstone_bridge.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Sandstone Bridge", card["name"])

    def test_normal_bfz_sure_strike(self):
        file_path = os.path.join(NORMAL_DIR, "bfz_sure_strike.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Sure Strike", card["name"])


class BlendingBackgroundCardIdentifierTest(TestCase):

    def test_blending_dtk_lightning_berseker(self):
        file_path = os.path.join(BLENDING_DIR, "dtk_lightning_berserker.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Lightning Berserker", card["name"])

    def test_blending_dtk_roast(self):
        file_path = os.path.join(BLENDING_DIR, "dtk_roast.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Roast", card["name"])

    def test_blending_frf_cunning_strike(self):
        file_path = os.path.join(BLENDING_DIR, "frf_cunning_strike.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Cunning Strike", card["name"])

    def test_blending_frf_formless_nurturing(self):
        file_path = os.path.join(BLENDING_DIR, "frf_formless_nurturing.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Formless Nurturing", card["name"])

    def test_blending_frf_lightform(self):
        file_path = os.path.join(BLENDING_DIR, "frf_lightform.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Lightform", card["name"])

    def test_blending_frf_tasigurs_cruelty(self):
        file_path = os.path.join(BLENDING_DIR, "frf_tasigurs_cruelty.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Tasigur's Cruelty", card["name"])

    def test_blending_frf_will_of_the_naga(self):
        file_path = os.path.join(BLENDING_DIR, "frf_will_of_the_naga.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Will of the Naga", card["name"])

    def test_blending_ori_blood_cursed_knight(self):
        file_path = os.path.join(BLENDING_DIR, "ori_blood_cursed_knight.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Blood-Cursed Knight", card["name"])

    def test_blending_ori_forest(self):
        file_path = os.path.join(BLENDING_DIR, "ori_forest.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Forest", card["name"])

    def test_blending_ori_mage_ring_bully(self):
        file_path = os.path.join(BLENDING_DIR, "ori_mage_ring_bully.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Mage-Ring Bully", card["name"])

    def test_blending_ori_might_of_the_masses(self):
        file_path = os.path.join(BLENDING_DIR, "ori_might_of_the_masses.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Might of the Masses", card["name"])

    def test_blending_ori_mountain(self):
        file_path = os.path.join(BLENDING_DIR, "ori_mountain.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Mountain", card["name"])

    def test_blending_ori_swamp(self):
        file_path = os.path.join(BLENDING_DIR, "ori_swamp.jpg")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Swamp", card["name"])

    def test_blending_ori_tower_geist(self):
        file_path = os.path.join(BLENDING_DIR, "ori_tower_geist.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Tower Geist", card["name"])

    def test_blending_ori_weight_of_the_underworld(self):
        file_path = os.path.join(BLENDING_DIR, "ori_weight_of_the_underworld.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Weight of the Underworld", card["name"])


class OrientationCardIdentifierTest(TestCase):

    def test_orientation_disperse_one(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_1.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Disperse", card["name"])

    def test_orientation_disperse_two(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_2.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Disperse", card["name"])

    def test_orientation_disperse_three(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_3.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Disperse", card["name"])

    def test_orientation_disperse_four(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_4.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Disperse", card["name"])

    def test_orientation_disperse_five(self):
        file_path = os.path.join(ORIENTATION_DIR, "ori_disperse_5.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Disperse", card["name"])


class PerspectiveCardIdentifierTest(TestCase):

    def test_perspective_valor_in_akros_one(self):
        file_path = os.path.join(PERSPECTIVE_DIR, "ori_valor_in_akros_1.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Valor in Akros", card["name"])

    def test_perspective_valor_in_akros_two(self):
        file_path = os.path.join(PERSPECTIVE_DIR, "ori_valor_in_akros_2.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Valor in Akros", card["name"])


class DamagedCardIdentifierTest(TestCase):

    def test_aven_battle_priest_one(self):
        file_path = os.path.join(DAMAGED_DIR, "ori_aven_battle_priest_1.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Aven Battle Priest", card["name"])

    def test_aven_battle_priest_two(self):
        file_path = os.path.join(DAMAGED_DIR, "ori_aven_battle_priest_2.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Aven Battle Priest", card["name"])

    def test_aven_battle_priest_three(self):
        file_path = os.path.join(DAMAGED_DIR, "ori_aven_battle_priest_3.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Aven Battle Priest", card["name"])


class BusyCardFinderTest(TestCase):

    def test_busy_scour_from_existence_one(self):
        file_path = os.path.join(BUSY_DIR, "bfz_scour_from_existence_1.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Scour from Existence", card["name"])

    def test_busy_scour_from_existence_two(self):
        file_path = os.path.join(BUSY_DIR, "bfz_scour_from_existence_2.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Scour from Existence", card["name"])

    def test_busy_scour_from_existence_three(self):
        file_path = os.path.join(BUSY_DIR, "bfz_scour_from_existence_3.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Scour from Existence", card["name"])

    def test_busy_bfz_stone_haven_medic_one(self):
        file_path = os.path.join(BUSY_DIR, "bfz_stone_haven_medic_1.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Stone Haven Medic", card["name"])

    def test_busy_bfz_stone_haven_medic_two(self):
        file_path = os.path.join(BUSY_DIR, "bfz_stone_haven_medic_2.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Stone Haven Medic", card["name"])

    def test_busy_bfz_stone_haven_medic_three(self):
        file_path = os.path.join(BUSY_DIR, "bfz_stone_haven_medic_3.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Stone Haven Medic", card["name"])

    def test_busy_bfz_stone_haven_medic_four(self):
        file_path = os.path.join(BUSY_DIR, "bfz_stone_haven_medic_4.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Stone Haven Medic", card["name"])

    def test_busy_dtk_gurmag_drowner_one(self):
        file_path = os.path.join(BUSY_DIR, "dtk_gurmag_drowner_1.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Gurmag Drowner", card["name"])

    def test_busy_dtk_gurmag_drowner_two(self):
        file_path = os.path.join(BUSY_DIR, "dtk_gurmag_drowner_2.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Gurmag Drowner", card["name"])

    def test_busy_dtk_gurmag_drowner_three(self):
        file_path = os.path.join(BUSY_DIR, "dtk_gurmag_drowner_3.JPG")
        card = identify_file(file_path, find_card=True)

        self.assertIsNotNone(card)
        self.assertEqual("Gurmag Drowner", card["name"])
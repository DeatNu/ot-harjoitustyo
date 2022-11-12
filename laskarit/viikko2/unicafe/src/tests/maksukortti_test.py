import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_muuttuu_oikein_kun_rahaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_kun_liian_vahan_rahaa(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_palauttaa_oikean_tuloksen(self):
        self.assertEqual(self.maksukortti.ota_rahaa(800), True)
        self.assertEqual(self.maksukortti.ota_rahaa(300), False)

    def test_lataaminen_toimii_kun_epanegatiivinen_summa(self):
        self.maksukortti.lataa_rahaa(12)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.12 euroa")



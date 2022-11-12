import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_oikea_maara_rahaa_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_ei_myynteje(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_riittava_rahamaara(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_edullinen_riittamaton_rahamaara(self):
        alussa = self.kassapaate.kassassa_rahaa
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alussa)

    def test_kateisosto_maukas_riittava_rahamaara(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukas_riittamaton_rahamaara(self):
        alussa = self.kassapaate.kassassa_rahaa
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alussa)

    def test_korttiosto_edullinen_riittava_rahamara(self):
        alussa = self.kassapaate.kassassa_rahaa
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 260)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alussa)

    def test_korttiosto_edullinen_riittamaton_rahamara(self):
        alussa = self.kassapaate.kassassa_rahaa
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alussa)

    def test_korttiosto_maukas_riittava_rahamara(self):
        alussa = self.kassapaate.kassassa_rahaa
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alussa)

    def test_korttiosto_maukas_riittamaton_rahamara(self):
        alussa = self.kassapaate.kassassa_rahaa
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alussa)

    def test_kortin_lataus_oikea_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 145)
        self.assertEqual(self.maksukortti.saldo, 645)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100145)

    def test_kortin_lataus_vaara_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -56)
        self.assertEqual(self.maksukortti.saldo, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)














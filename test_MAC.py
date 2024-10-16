import unittest
from MACAddress import MACAddress

class testMAC(unittest.TestCase):
    def test_is_valid_Valid_Colon_separated(self):
        self.assertEqual(MACAddress.is_valid('00:25:96:FF:fe:1a'), True)
    def test_is_valid_Valid_Hyphen_separated(self):
        self.assertEqual(MACAddress.is_valid('00-25-96-FF-fe-1a'), True)
    def test_is_valid_Valid_Dot_separated(self):
        self.assertEqual(MACAddress.is_valid('0025.96FF.fe1a'), True)
    def test_is_valid_Valid_Hexadecimal_string(self):
        self.assertEqual(MACAddress.is_valid('002596FFfe1a'), True)
    def test_is_valid_InizioSbagliato(self):
        self.assertEqual(MACAddress.is_valid(' 00:25:96:FF:fe:1a:34:56'), False)
    def test_is_valid_FineSbagliata(self):
        self.assertEqual(MACAddress.is_valid('00:25:96:FF:fe:1a:34:56 '), False)
    def test_is_valid_NoHex(self):
        self.assertEqual(MACAddress.is_valid('00:2u:96:FF:FE:12:34:56'), False)
    def test_is_valid_No2Elements(self):
        self.assertEqual(MACAddress.is_valid('00:25:96e:FF:FE:12:34:56'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96:F:FE:12:34:56'), False)
    def test_is_valid_Troppi(self):
        self.assertEqual(MACAddress.is_valid('00:25:96:FF:FE:12:34:56:00:25:96:FF:FE:112'), False)
    def test_is_valid_Pochi(self):
        self.assertEqual(MACAddress.is_valid('00'), False)
        self.assertEqual(MACAddress.is_valid('00:25'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96:FF'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96:FF:fe'), False)

    def test___init___Valid_Colon_separated(self):
        mac = MACAddress('18:C0:4D:87:74:91')
        self.assertEqual(mac._macAddress, '18c04d877491')
    def test___init___Valid_Hyphen_separated(self):
        mac = MACAddress('18-C0-4D-87-74-91')
        self.assertEqual(mac._macAddress, '18c04d877491')
    def test___init___Valid_Dot_separated(self):
        mac = MACAddress('18c0.4d87.7491')
        self.assertEqual(mac._macAddress, '18c04d877491')
    def test___init___Valid_Hexadecimal_string(self):
        mac = MACAddress('18c04d877491')
        self.assertEqual(mac._macAddress, '18c04d877491')
if __name__ == '__main__':
    unittest.main()

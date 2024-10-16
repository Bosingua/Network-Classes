import unittest
from MACAddress import MACAddress

class testMAC(unittest.TestCase):
    def test_is_valid(self):
        self.assertEqual(MACAddress.is_valid('00:25:96:FF:fe:1a'), True)
        self.assertEqual(MACAddress.is_valid('00-25-96-FF-fe-1a'), True)
        self.assertEqual(MACAddress.is_valid('0025.96FF.fe1a'), True)
        self.assertEqual(MACAddress.is_valid('002596FFfe1a'), True)
        self.assertEqual(MACAddress.is_valid(' 00:25:96:FF:fe:1a:34:56'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96:FF:fe:1a:34:56 '), False)
        self.assertEqual(MACAddress.is_valid('00:2u:96:FF:FE:12:34:56'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96e:FF:FE:12:34:56'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96:F:FE:12:34:56'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96:FF:FE:12:34:56:00:25:96:FF:FE:112'), False)
        self.assertEqual(MACAddress.is_valid('00'), False)
        self.assertEqual(MACAddress.is_valid('00:25'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96:FF'), False)
        self.assertEqual(MACAddress.is_valid('00:25:96:FF:fe'), False)

    def test___init__(self):
        self.assertEqual(MACAddress('18:C0:4D:87:74:91')._macAddress, '18c04d877491')
        self.assertEqual(MACAddress('18-C0-4D-87-74-91')._macAddress, '18c04d877491')
        self.assertEqual(MACAddress('18c0.4d87.7491')._macAddress,    '18c04d877491')
        self.assertEqual(MACAddress('18c04d877491')._macAddress,      '18c04d877491')
        with self.assertRaises(ValueError) as error:
            MACAddress(' 00:25:96:FF:fe:1a:34:56')
        self.assertEqual(str(error.exception), 'Invalid MAC address')

    def test_in_Colon_separated_format(self):
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F').in_Colon_separated_format(),      '18:C0:4D:87:74:8F')
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F').in_Colon_separated_format(False), '18:c0:4d:87:74:8f')

    def test_in_Hyphen_separated_format(self):
        self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_Hyphen_separated_format(),      '18-C0-4D-87-74-8F')
        self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_Hyphen_separated_format(False), '18-c0-4d-87-74-8f')

    def test_in_dot_separated_format(self):
        self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_dot_separated_format(True), '18C0.4D87.748F')
        self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_dot_separated_format(),     '18c0.4d87.748f')

    def test___eq__(self):
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F') == MACAddress('18:C0:4D:87:74:8F'), True)
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F') == '18:C0:4D:87:74:8F',             True)
        self.assertEqual('18-C0-4D-87-74-8Fd'            == MACAddress('18:C0:4D:87:74:8F'), False)
        self.assertEqual('0025.96FF.fe1a'                == MACAddress('18:C0:4D:87:74:8F'), False)

if __name__ == '__main__':
    unittest.main(verbosity=3)

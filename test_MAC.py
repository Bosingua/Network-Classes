import unittest
from MACAddress import MACAddress
from dataclasses import FrozenInstanceError

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
        self.assertEqual(MACAddress.is_valid(3253456), False)
        self.assertEqual(MACAddress.is_valid([3253456,'R']), False)
        self.assertEqual(MACAddress.is_valid(([3253456,'R'], 4, 'dede')), False)

    def test___new__(self):
        self.assertEqual(MACAddress('18:C0:4D:87:74:91')._mac_address, '18c04d877491')
        self.assertEqual(MACAddress('18-C0-4D-87-74-91')._mac_address, '18c04d877491')
        self.assertEqual(   MACAddress('18c0.4d87.7491')._mac_address, '18c04d877491')
        self.assertEqual(     MACAddress('002596FFfe1a')._mac_address, '002596fffe1a')
        with self.assertRaises(ValueError) as error:
            MACAddress('Not a valid string for MAC address')
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
        self.assertEqual(1111111111111111                == MACAddress('18:C0:4D:87:74:8F'), False)

    def test_immutable(self):
        mac = MACAddress('18-C0-4D-87-74-8F')
        with self.assertRaises(FrozenInstanceError) as error:
            mac._mac_address = '='
        self.assertEqual(str(error.exception), "cannot assign to field '_mac_address'")

if __name__ == '__main__':
    unittest.main(verbosity=3)
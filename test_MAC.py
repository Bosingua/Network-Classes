import unittest
from MACAddress import MACAddress

class testMAC(unittest.TestCase):

    def test___init__(self):
        self.assertEqual(MACAddress('18:C0:4D:87:74:91')._mac_address, '18c04d877491')
        self.assertEqual(MACAddress('18-C0-4D-87-74-91')._mac_address, '18c04d877491')
        self.assertEqual(   MACAddress('18c0.4d87.7491')._mac_address, '18c04d877491')
        self.assertEqual(     MACAddress('002596FFfe1a')._mac_address, '002596fffe1a')
        self.assertEqual(MACAddress('000110001100000001001101100001110111010010001111')._mac_address, '18c04d87748f')

        test_input = [' 00:25:96:FF:fe:1a', '96:FF:fe:1a:34:56 ', '00:2u:96:FF:FE:12', '00:25:96e:FF:FE:12',
        '00:25:96:F:FE:12', '00:25:96:FF:FE:112', '00', '00:25', '00:25:96', '00:25:96:FF', '00:25:96:FF:fe',
        2, [6,'R'], ([51,'R'], 4, 'dede'), '002:5:96:FF:fe:1a', '002.596FF.fe1a']
        for input in test_input:
            with self.assertRaises(ValueError) as error:MACAddress(input)
            self.assertEqual(str(error.exception), 'Invalid MAC address')

    def test_in_Colon_separated_format(self):
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F').in_Colon_separated_format()     , '18:C0:4D:87:74:8F')
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F').in_Colon_separated_format(False), '18:c0:4d:87:74:8f')

    def test_in_Hyphen_separated_format(self):
        self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_Hyphen_separated_format()     , '18-C0-4D-87-74-8F')
        self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_Hyphen_separated_format(False), '18-c0-4d-87-74-8f')

    def test_in_dot_separated_format(self):
        self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_dot_separated_format(True), '18C0.4D87.748F')
        self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_dot_separated_format()    , '18c0.4d87.748f')

    def test_in_bin(self):
        self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_bin(), '000110001100000001001101100001110111010010001111')
        self.assertEqual(MACAddress('00:00:4D:87:74:8F').in_bin(), '000000000000000001001101100001110111010010001111')
        # self.assertEqual(MACAddress('18:C0:4D:87:74:8F').in_bin()    , '18c0.4d87.748f')

    def test___eq__(self):
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F') == MACAddress('18:C0:4D:87:74:8F'), True)
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F') == '18:C0:4D:87:74:8F'            , True)
        self.assertEqual(            '18-C0-4D-87-74-8F' == MACAddress('18:C0:4D:87:74:8F'), True)
        # self.assertEqual(               '0025.96FF.fe1a' == MACAddress('18:C0:4D:87:74:8F'), False)
        test_input = [' 00:25:96:FF:fe:1a', '96:FF:fe:1a:34:56 ', '00:2u:96:FF:FE:12', '00:25:96e:FF:FE:12',
        '00:25:96:F:FE:12', '00:25:96:FF:FE:112', '00', '00:25', '00:25:96', '00:25:96:FF', '00:25:96:FF:fe',
        2, [6,'R'], ([51,'R'], 4, 'dede'),'002:5:96:FF:fe:1a', '0025.96FF.fe1a', '18C:0:4D:87:74:8F']
        for input in test_input:
            self.assertEqual(input == MACAddress('18:C0:4D:87:74:8F'), False, f'input = {input}')
            self.assertEqual(MACAddress('18:C0:4D:87:74:8F') == input, False, f'input = {input}')

    def test___ne__(self):
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F') != MACAddress('18:C0:4D:87:74:8F'), False)
        self.assertEqual(MACAddress('18-C0-4D-87-74-8F') != '18:C0:4D:87:74:8F'            , False)
        self.assertEqual(            '18-C0-4D-87-74-8F' != MACAddress('18:C0:4D:87:74:8F'), False)
        self.assertEqual(               '0025.96FF.fe1a' != MACAddress('18:C0:4D:87:74:8F'), True)

    def test_random_generator(self):
        random_mac = MACAddress.random_generator()
        self.assertEqual(random_mac._mac_address, MACAddress.random_generator(random_mac._mac_address)._mac_address)
        with self.assertRaises(TypeError) as error: MACAddress.random_generator([1,5])
        self.assertEqual(str(error.exception), "Prefix must be a 'str' type")
        with self.assertRaises(ValueError) as error: MACAddress.random_generator('ged1695')
        self.assertEqual(str(error.exception), 'Not valid prefix')
        with self.assertRaises(ValueError) as error: MACAddress.random_generator('aaaaaaaaaaaaaaaaa15165bb')
        self.assertEqual(str(error.exception), 'Not valid prefix')

    def test_immutable(self):
        mac = MACAddress('18-C0-4D-87-74-8F')
        with self.assertRaises(ValueError) as error: mac._mac_address = '='
        self.assertEqual(str(error.exception), "cannot assign to field '_mac_address'")
        with self.assertRaises(ValueError) as error: mac._mac_address = '0025.96FF.fe1a'
        self.assertEqual(str(error.exception), "cannot assign to field '_mac_address'")
        with self.assertRaises(ValueError) as error: mac._qualche_attributo_ = '0025.96FF.fe1a'
        self.assertEqual(str(error.exception), "cannot assign to field '_qualche_attributo_'")
        with self.assertRaises(ValueError) as error: del mac._mac_address
        self.assertEqual(str(error.exception), "cannot assign to field '_mac_address'")

if __name__ == '__main__':
    unittest.main(verbosity=1)

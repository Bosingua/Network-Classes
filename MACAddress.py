import re

class MACAddress:

    def __init__(self, macAddress : str):
        if not self.is_valid(macAddress):
            raise ValueError('Invalid MAC address')
        
        if MACAddress._formato == 'Colon-separated':
            self._macAddress = macAddress.replace(":", "").lower()
        elif MACAddress._formato == 'Hyphen-separated':
            self._macAddress = macAddress.replace("-", "").lower()
        elif MACAddress._formato == 'Dot-separated':
            self._macAddress = macAddress.replace(".", "").lower()
        elif MACAddress._formato == 'Hexadecimal string':
            self._macAddress = macAddress.lower()

    @staticmethod
    def is_valid(mac_address : str) -> bool:
        colon_separated_patten  = re.compile(r'([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})')
        hyphen_separated_patten = re.compile(r'([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2})')
        dot_separated_patten    = re.compile(r'([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})')
        hexadecimal_patten      = re.compile(r'([0-9A-Fa-f]{12})')

        if re.fullmatch(colon_separated_patten, mac_address):
            MACAddress._formato = 'Colon-separated'
            return True
        elif re.fullmatch(hyphen_separated_patten, mac_address):
            MACAddress._formato = 'Hyphen-separated'
            return True
        elif re.fullmatch(dot_separated_patten, mac_address):
            MACAddress._formato = 'Dot-separated'
            return True
        elif re.fullmatch(hexadecimal_patten, mac_address):
            MACAddress._formato = 'Hexadecimal string'
            return True
        else:
            return False

    def in_Colon_separated_format(self) -> str:
        return ':'.join([self._macAddress[i:i+2].upper() for i in range(0, 12, 2)])

    def in_Hyphen_separated_format(self) -> str:
        return '-'.join([self._macAddress[i:i+2].upper() for i in range(0, 12, 2)])

    def in_dot_separated_format(self) -> str:
        return '.'.join([self._macAddress[i:i+4] for i in range(0, 12, 4)])

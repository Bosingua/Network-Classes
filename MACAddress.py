import re

class MACAddress:

    _formati_mac = {'Colon-separated'    : {'separator' : ":",   'pattern' : re.compile(r'[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}')},
                    'Hyphen-separated'   : {'separator' : "-",   'pattern' : re.compile(r'[0-9A-Fa-f]{2}(-[0-9A-Fa-f]{2}){5}')},
                    'Dot-separated'      : {'separator' : ".",   'pattern' : re.compile(r'[0-9A-Fa-f]{4}(.[0-9A-Fa-f]{4}){2}')},
                    'Hexadecimal string' : {'separator' : False, 'pattern' : re.compile(r'[0-9A-Fa-f]{12}')}}

    @staticmethod
    def is_valid(mac_address : str) -> bool:
        for format_name, pattern in MACAddress._formati_mac.items():
            pattern = pattern['pattern']
            if re.fullmatch(pattern, mac_address):
                MACAddress._formato = format_name
                return True
        return False

    def __init__(self, macAddress : str):
        if not self.is_valid(macAddress):
            raise ValueError('Invalid MAC address')

        separator = MACAddress._formati_mac[MACAddress._formato]['separator']
        self._macAddress = macAddress.replace(separator, "").lower() if separator else macAddress.lower()

    def _format_mac_address(self, separator : str, upcase : bool, len : int = 2) -> str:
        macAddress = self._macAddress.upper() if upcase else self._macAddress
        return separator.join([macAddress[i:i+len] for i in range(0, 12, len)])

    def in_Colon_separated_format(self, upcase : bool = True) -> str:
        return self._format_mac_address(":", upcase)

    def in_Hyphen_separated_format(self, upcase : bool = True) -> str:
        return self._format_mac_address("-", upcase)

    def in_dot_separated_format(self, upcase : bool = False) -> str:
        return self._format_mac_address(".", upcase, 4)

    def __eq__(self, other) -> bool:
        if not isinstance(other, MACAddress):
            try:
                other = MACAddress(other)
            except:
                return False
        return self._macAddress == other._macAddress

import re

class MACAddress:

    _formati_mac = {'Colon-separated'    : {'separator' : ":",   'pattern' : re.compile(r'[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}')},
                    'Hyphen-separated'   : {'separator' : "-",   'pattern' : re.compile(r'[0-9A-Fa-f]{2}(-[0-9A-Fa-f]{2}){5}')},
                    'Dot-separated'      : {'separator' : ".",   'pattern' : re.compile(r'[0-9A-Fa-f]{4}(.[0-9A-Fa-f]{4}){2}')},
                    'Hexadecimal string' : {'separator' : False, 'pattern' : re.compile(r'[0-9A-Fa-f]{12}')}}

    @staticmethod
    def is_valid(mac_address) -> bool:
        if isinstance(mac_address, str):
            for format_name, pattern in MACAddress._formati_mac.items():
                pattern = pattern['pattern']
                if re.fullmatch(pattern, mac_address):
                    MACAddress._formato = format_name
                    return True
        return False

    def mac_in_memory(macAddress : str) -> str:
        separator = MACAddress._formati_mac[MACAddress._formato]['separator']
        return macAddress.replace(separator, "").lower() if separator else macAddress.lower()

    def __new__(cls, macAddress : str):
        if not cls.is_valid(macAddress):
            raise ValueError('Invalid MAC address')
        cls._macAddress = MACAddress.mac_in_memory(macAddress)
        return super(MACAddress, cls).__new__(cls)

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
            return self._macAddress == MACAddress.mac_in_memory(other) if MACAddress.is_valid(other) else False
        return self._macAddress == other._macAddress
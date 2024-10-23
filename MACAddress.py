from re import compile, fullmatch
from dataclasses import dataclass

@dataclass(frozen=True)
class MACAddress:
    _original_input : str

    _formati_mac = {'Colon-separated'    : {'separator' : ":",   'pattern' : compile(r'[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}')},
                    'Hyphen-separated'   : {'separator' : "-",   'pattern' : compile(r'[0-9A-Fa-f]{2}(-[0-9A-Fa-f]{2}){5}')},
                    'Dot-separated'      : {'separator' : ".",   'pattern' : compile(r'[0-9A-Fa-f]{4}(.[0-9A-Fa-f]{4}){2}')},
                    'Hexadecimal string' : {'separator' : False, 'pattern' : compile(r'[0-9A-Fa-f]{12}')}}

    def check_format(mac_address: str) -> str:
        for format_name, pattern in MACAddress._formati_mac.items():
            if fullmatch(pattern['pattern'], mac_address):
                return format_name
        return 'None'
                
    @staticmethod
    def is_valid(mac_address) -> bool:
        if isinstance(mac_address, str):
            MACAddress._format = MACAddress.check_format(mac_address)
            return False if MACAddress._format == 'None' else True
        return False

    def mac_in_memory(macAddress : str) -> str:
        separator = MACAddress._formati_mac[MACAddress._format]['separator']
        return macAddress.replace(separator, "").lower() if separator else macAddress.lower()

    def __post_init__(self):
        if not self.is_valid(self._original_input):
            raise ValueError('Invalid MAC address')
        MACAddress._mac_address = MACAddress.mac_in_memory(self._original_input)

    def _format_mac_address(self, separator : str, upcase : bool, len : int = 2) -> str:
        macAddress = self._mac_address.upper() if upcase else self._mac_address
        return separator.join([macAddress[i:i+len] for i in range(0, 12, len)])

    def in_Colon_separated_format(self, upcase : bool = True) -> str:
        return self._format_mac_address(":", upcase)

    def in_Hyphen_separated_format(self, upcase : bool = True) -> str:
        return self._format_mac_address("-", upcase)

    def in_dot_separated_format(self, upcase : bool = False) -> str:
        return self._format_mac_address(".", upcase, 4)

    def __eq__(self, other) -> bool:
        if not isinstance(other, MACAddress):
            return self._mac_address == MACAddress.mac_in_memory(other) if MACAddress.is_valid(other) else False
        return self._mac_address == other._mac_address
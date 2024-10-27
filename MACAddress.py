from re import compile, fullmatch

class MACAddress:

    _formati_mac = {'Colon-separated'    : {'separator' : ":", 'pattern' : compile(r'[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}')},
                    'Hyphen-separated'   : {'separator' : "-", 'pattern' : compile(r'[0-9A-Fa-f]{2}(-[0-9A-Fa-f]{2}){5}')},
                    'Dot-separated'      : {'separator' : ".", 'pattern' : compile(r'[0-9A-Fa-f]{4}(.[0-9A-Fa-f]{4}){2}')},
                    'Hexadecimal string' : {'separator':False, 'pattern' : compile(r'[0-9A-Fa-f]{12}')}}

    def _check_format(self, mac_address: str) -> str:
        for format_name, pattern in self._formati_mac.items():
            if fullmatch(pattern['pattern'], mac_address):
                return format_name
        return 'None'

    def _is_valid(self, input) -> bool:
        return (False if self._check_format(input) == 'None' else True) if isinstance(input, str) else False

    def _mac_in_memory(self, mac : str) -> str:
        separator = self._formati_mac[self._check_format(mac)]['separator']
        return mac.replace(separator, "").lower() if separator else mac.lower()

    def __init__(self, input : str):
        self._mac_address = input

    def __setattr__(self, name, value):
        if hasattr(self, '_mac_address'):
            raise ValueError(f"cannot assign to field '{name}'")
        if not self._is_valid(value):
            raise ValueError('Invalid MAC address')
        super().__setattr__(name, self._mac_in_memory(value))

    def _format_mac_address(self, separator : str, upcase : bool, len : int = 2) -> str:
        mac = self._mac_address.upper() if upcase else self._mac_address
        return separator.join([mac[i:i+len] for i in range(0, 12, len)])

    def in_Colon_separated_format(self, upcase : bool = True) -> str:
        return self._format_mac_address(":", upcase)

    def in_Hyphen_separated_format(self, upcase : bool = True) -> str:
        return self._format_mac_address("-", upcase)

    def in_dot_separated_format(self, upcase : bool = False) -> str:
        return self._format_mac_address(".", upcase, 4)

    def __eq__(self, other) -> bool:
        if not isinstance(other, MACAddress):
            return self._mac_address == self._mac_in_memory(other) if self._is_valid(other) else False
        return self._mac_address == other._mac_address

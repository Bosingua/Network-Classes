from re import compile, fullmatch
from random import randint

class MACAddress:

    def _is_valid(self, input) -> bool:
        if not isinstance(input, str): return False
        return fullmatch(compile(r'[\dA-Fa-f]{12}'), input.translate(str.maketrans('', '', ':-.')).lower())

    def _mac_in_memory(self, mac : str) -> str: return mac.translate(str.maketrans('', '', ':-.')).lower()

    def __init__(self, input : str) -> None: self._mac_address = input

    def __setattr__(self, name : str, value):
        if hasattr(self, '_mac_address'): raise ValueError(f"cannot assign to field '{name}'")
        if not self._is_valid(value): raise ValueError('Invalid MAC address')
        super().__setattr__(name, self._mac_in_memory(value))

    def _format_mac_address(self, separator : str, upcase : bool, len : int = 2) -> str:
        mac = self._mac_address.upper() if upcase else self._mac_address
        return separator.join([mac[i:i+len] for i in range(0, 12, len)])

    def in_Colon_separated_format(self, upcase : bool = True) -> str: return self._format_mac_address(":", upcase)

    def in_Hyphen_separated_format(self, upcase : bool = True) -> str: return self._format_mac_address("-", upcase)

    def in_dot_separated_format(self, upcase : bool = False) -> str: return self._format_mac_address(".", upcase, 4)

    def __add__(self): raise ValueError

    __radd__ = __sub__ =__truediv__ = __div__ = __add__

    def __eq__(self, other) -> bool:
        if isinstance(other, MACAddress): return self._mac_address == other._mac_address
        return self._mac_address == self._mac_in_memory(other) if self._is_valid(other) else False

    def __hash__(self) -> str: return self._mac_address

    def __bool__(self) -> bool: return True

    @staticmethod
    def random_generator(input = ''):
        input = input.translate(str.maketrans('', '', ':-.')).lower()
        if len(input) > 13 and not fullmatch(compile(r'[\dA-Fa-f]?'), input): raise ValueError
        return MACAddress(input + ''.join([format(randint(0,15), 'x') for _ in range(12 - len(input))]))

from re import fullmatch
from random import randint

class MACAddress:

    def _is_valid(self, input) -> bool:
        if not isinstance(input, str): return False
        input = input.lower()
        pattern = r'[\da-f]{12}|[\da-f]{2}([:-][\da-f]{2}){5}|([\da-f]{4}\.){2}[\da-f]{4}'
        if not fullmatch(pattern, input): return False
        return fullmatch(r'[\da-f]{12}', input.translate(str.maketrans('', '', ':-.')))

    def __init__(self, input: str) -> None: self._mac_address = input

    def __setattr__(self, name: str, value: str) -> None:
        if hasattr(self, '_mac_address'): raise ValueError(f"cannot assign to field '{name}'")
        if not self._is_valid(value): raise ValueError('Invalid MAC address')
        super().__setattr__(name, value.translate(str.maketrans('','',':-.')).lower())

    def __delattr__(self, name): raise ValueError(f"cannot assign to field '{name}'")

    def _format_mac_address(self, separator: str, upcase: bool, len_block: int = 2) -> str:
        mac = self._mac_address.upper() if upcase else self._mac_address
        return separator.join([mac[i:i+len_block] for i in range(0, 12, len_block)])

    def in_Colon_separated_format(self, upcase: bool = True) -> str: return self._format_mac_address(":", upcase)

    def in_Hyphen_separated_format(self, upcase: bool = True) -> str: return self._format_mac_address("-", upcase)

    def in_dot_separated_format(self, upcase: bool = False) -> str: return self._format_mac_address(".", upcase, 4)

    def __add__(self): raise ValueError(f"unsupported operator for 'MACAddress'")

    __radd__ = __sub__ =__truediv__ = __div__ = __mod__ = __pow__ = __floordiv__ = __add__
    __rsub__ =__rtruediv__ = __rdiv__ = __rmod__ = __rpow__ = __rfloordiv__ = __add__
    __lt__ = __le__ = __ge__ = __gt__ = __add__

    def __eq__(self, other) -> bool:
        if isinstance(other, MACAddress): return self._mac_address == other._mac_address
        if isinstance(other, str):
            pattern = r'[\da-f]{12}|[\da-f]{2}([:-][\da-f]{2}){5}|([\da-f]{4}\.){2}[\da-f]{4}'
            if not fullmatch(pattern, other.lower()): return False
            return self._mac_address == other.translate(str.maketrans('','',':-.')).lower()
        return False

    def __ne__(self, other) -> bool: return not self.__eq__(other)

    def __hash__(self) -> str: return self._mac_address

    def __bool__(self) -> bool: return True

    @staticmethod
    def random_generator(input: str = ''):
        if not isinstance(input, str): raise TypeError("Prefix must be a 'str' type")
        input = input.translate(str.maketrans('', '', ':-.')).lower()
        if not fullmatch(r'[\da-f]{0,12}', input): raise ValueError('Not valid prefix')
        return MACAddress(f'{input}{''.join([format(randint(0, 15), 'x') for _ in range(12 - len(input))])}')

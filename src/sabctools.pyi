from typing import Tuple, Optional, IO
from ssl import SSLSocket

__version__: str
openssl_linked: bool
simd: str

def yenc_decode(raw_data: bytearray) -> Tuple[str, int, int, int, Optional[int]]: ...
def yenc_encode(input_string: bytes) -> Tuple[bytes, int]: ...

def unlocked_ssl_recv_into(ssl_socket: SSLSocket, buffer: memoryview) -> int: ...

def crc32_combine(crc1: int, crc2: int, length: int) -> int: ...
def crc32_multiply(crc1: int, crc2: int) -> int: ...
def crc32_xpow8n(n: int) -> int: ...
def crc32_xpown(n: int) -> int: ...
def crc32_zero_unpad(crc1: int, length: int) -> int: ...

def sparse(file: IO, length: int) -> None: ...

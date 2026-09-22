"""Educational hash demonstration, not secure QKD privacy amplification."""

import hashlib


def hash_bits(bits: list[int]) -> str:
    """Return the SHA-256 hex digest of a validated bit sequence."""
    if not bits:
        raise ValueError("Bit sequence must not be empty")
    if any(bit not in (0, 1) for bit in bits):
        raise ValueError("Bit sequence must contain only 0 and 1")

    encoded_bits = "".join(str(bit) for bit in bits).encode("ascii")
    return hashlib.sha256(encoded_bits).hexdigest()
"""Educational challenge-response demonstration, not PKI or TLS."""

import hashlib
import hmac
import secrets


def create_challenge() -> bytes:
    """Generate a fresh challenge."""
    return secrets.token_bytes(32)


def respond_to_challenge(secret_key: bytes, challenge: bytes) -> bytes:
    """Compute a response using a shared secret."""
    return hmac.new(secret_key, challenge, hashlib.sha256).digest()


def verify_response(
    secret_key: bytes,
    challenge: bytes,
    response: bytes,
) -> bool:
    """Check whether the response matches the expected value."""
    expected = respond_to_challenge(secret_key, challenge)
    return hmac.compare_digest(expected, response)

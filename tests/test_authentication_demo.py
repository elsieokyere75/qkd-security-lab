from src.authentication_demo import (
    create_challenge,
    respond_to_challenge,
    verify_response,
)


def test_challenge_is_32_bytes():
    assert len(create_challenge()) == 32


def test_correct_secret_verifies():
    secret = b"shared-demo-secret"
    challenge = create_challenge()
    response = respond_to_challenge(secret, challenge)

    assert verify_response(secret, challenge, response)


def test_wrong_secret_fails():
    secret = b"shared-demo-secret"
    challenge = create_challenge()
    response = respond_to_challenge(secret, challenge)

    assert not verify_response(
        b"wrong-secret", challenge, response
    )


def test_modified_challenge_fails():
    secret = b"shared-demo-secret"
    challenge = create_challenge()
    response = respond_to_challenge(secret, challenge)

    modified_challenge = bytes([challenge[0] ^ 1]) + challenge[1:]

    assert not verify_response(
        secret, modified_challenge, response
    )
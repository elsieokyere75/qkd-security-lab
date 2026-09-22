from src.architecture_model import Architecture, describe_architecture


def test_warns_when_qkd_channel_is_unauthenticated():
    design = Architecture(
        qkd_enabled=True,
        pqc_enabled=True,
        pki_enabled=True,
        classical_channel_authenticated=False,
    )

    descriptions = describe_architecture(design)

    assert (
        "WARNING: QKD requires authenticated classical communication"
        in descriptions
    )


def test_no_authentication_warning_when_marked_authenticated():
    design = Architecture(
        qkd_enabled=True,
        pqc_enabled=True,
        pki_enabled=True,
        classical_channel_authenticated=True,
    )

    descriptions = describe_architecture(design)

    assert not any(item.startswith("WARNING:") for item in descriptions)


def test_pqc_only_design_does_not_claim_qkd():
    design = Architecture(
        qkd_enabled=False,
        pqc_enabled=True,
        pki_enabled=False,
        classical_channel_authenticated=False,
    )

    assert describe_architecture(design) == [
        "PQC: proposed key establishment or authentication"
    ]
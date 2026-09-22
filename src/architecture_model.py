"""Conceptual QKD, PQC, and PKI architecture model."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Architecture:
    qkd_enabled: bool
    pqc_enabled: bool
    pki_enabled: bool
    classical_channel_authenticated: bool


def describe_architecture(design: Architecture) -> list[str]:
    """Describe components and flag a missing QKD prerequisite."""
    components = []

    if design.qkd_enabled:
        components.append("QKD: proposed source of shared key material")

    if design.pqc_enabled:
        components.append("PQC: proposed key establishment or authentication")

    if design.pki_enabled:
        components.append("PKI: certificate-based identity and key binding")

    if design.qkd_enabled and not design.classical_channel_authenticated:
        components.append(
            "WARNING: QKD requires authenticated classical communication"
        )

    return components
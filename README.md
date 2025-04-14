# Kyber Club PQC Tools

Welcome to a collection of resources and code samples for exploring quantum-safe cryptography, powered by [Kyber Club](https://kyber.club).

## Website
[Kyber Club](https://kyber.club) offers experimental tools for post-quantum cryptography, compliant with NIST standards like FIPS 203 (ML-KEM) and beyond. Use these tools for research and education to prepare for a quantum-safe future.

## Information about Key Encapsulation Mechanisms (KEM)
Key Encapsulation Mechanisms (KEMs) securely share cryptographic keys over insecure networks, essential for quantum-safe communication. Below are two KEMs supported by Kyber Club:

- **FIPS 203 / ML-KEM / Kyber** - A NIST-standardised KEM based on the Kyber algorithm, offering efficient, quantum-resistant key exchange. Explore tools for ML-KEM-512, 768, and 1024 at [Kyber Club’s FIPS 203 page](https://kyber.club/fips203).
- **FrodoKEM** - A lattice-based KEM designed for conservative security, ideal for PQC research. Learn more and try FrodoKEM-640-AES, 976-AES, and 1344-AES at [Kyber Club’s FrodoKEM page](https://kyber.club/frodokem).

## KEM Key Generation / Encryption / Decryption
Kyber Club provides user-friendly tools to experiment with KEM operations for research purposes:

- **Key Generation**: Create quantum-safe keypairs for ML-KEM or FrodoKEM. Start with [FIPS 203 key generation](https://kyber.club/fips203-gen) or [FrodoKEM key generation](https://kyber.club/frodokem-gen).
- **Encryption (Encapsulation)**: Securely encapsulate shared secrets using a recipient’s public key. Try [ML-KEM encapsulation](https://kyber.club/fips203-encrypt) or [FrodoKEM encapsulation](https://kyber.club/frodokem-encrypt).
- **Decryption (Decapsulation)**: Recover secrets with a private key. Use [ML-KEM decapsulation](https://kyber.club/fips203-decrypt) or [FrodoKEM decapsulation](https://kyber.club/frodokem-decrypt).

---

*Contributed by Santosh Pandit (@beatquantum). For issues or suggestions, open a GitHub issue or visit [Kyber Club’s contact page](https://kyber.club/contact).*

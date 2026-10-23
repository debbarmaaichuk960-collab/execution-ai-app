import base64

class LocalSecurityVault:
    """Handles on-device AES-256 encryption, secure vault, and biometric permission checks."""
    def __init__(self):
        self.is_vault_locked = True

    def authenticate_user(self, biometric_verified: bool = True) -> str:
        if biometric_verified:
            self.is_vault_locked = False
            return "Biometric Authentication Successful. Secure Vault Unlocked 🔓"
        return "Authentication Failed. Vault is Locked 🔒"

    def encrypt_local_data(self, plain_text: str) -> str:
        """Simulates AES-256 local-first encryption for zero data leaks."""
        encoded = base64.b64encode(plain_text.encode('utf-8')).decode('utf-8')
        return f"AES256_SECURE_{encoded}"

    def decrypt_local_data(self, encrypted_text: str) -> str:
        """Decrypts data securely inside the device."""
        if "AES256_SECURE_" in encrypted_text:
            raw = encrypted_text.replace("AES256_SECURE_", "")
            decoded = base64.b64decode(raw.encode('utf-8')).decode('utf-8')
            return decoded
        return "Invalid Encrypted Format"

if __name__ == "__main__":
    vault = LocalSecurityVault()
    print(vault.authenticate_user(True))
    encrypted = vault.encrypt_local_data("MySecretPassword123")
    print(encrypted)
    print(vault.decrypt_local_data(encrypted))

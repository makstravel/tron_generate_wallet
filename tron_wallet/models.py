from django.db import models
from .services.encryption_service import encrypt_data, decrypt_data

class TronWallet(models.Model):
    """
    Модель для хранения информации о Tron-кошельке, включая адрес,
    приватный ключ, мнемоническую фразу и дату создания.
    """

    # Поле для хранения адреса кошелька
    address = models.CharField(max_length=255, unique=True)
    mnemonic = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        self.mnemonic = encrypt_data(self.mnemonic)
        super().save(*args, **kwargs)

    def get_mnemonic(self):
        return decrypt_data(self.mnemonic)
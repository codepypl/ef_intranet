from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    # Nadpisujemy login, aby był e-mailem
    username = None
    email = models.EmailField('Adres e-mail', unique=True)

    # Dane z Azure Entra ID
    azure_id = models.UUIDField('Azure Object ID', unique=True, null=True, blank=True)

    # Dodatkowe pola firmowe
    job_title = models.CharField('Stanowisko', max_length=150, blank=True)
    department = models.CharField('Dział', max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Django standardowo wymaga e-maila, tutaj go już mamy

    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Pracownicy"

    def __str__(self):
        return self.email
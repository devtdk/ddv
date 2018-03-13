from django.db import models
from django.core.validators import RegexValidator


class Type(models.Model):
    name = models.CharField("Nazwa", help_text="Dokładnie 4 znaki, tylko litery lub cyfry", max_length=4, unique=True, validators=[RegexValidator(regex='^[a-zA-Z0-9]{4}$', message='Wpisz dokładnie 4 znaki. Dozwolone są tylko litery (bez polskich znaków) oraz cyfry.', code='nomatch')])

    class Meta:
        verbose_name = "Typ"
        verbose_name_plural = "Typy"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Type, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

from django.db import models

class iletisim_mesaj(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField
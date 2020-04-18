from django.db import models
from wholesaler.models import Wholesaler


class Article(models.Model):
    # After the bnn-3 specification with an additional wholesaler field
    artikelNr = models.CharField('ArtikelNr', max_length=14, primary_key=True)

    wholesaler = models.ForeignKey(Wholesaler, on_delete=models.DO_NOTHING)

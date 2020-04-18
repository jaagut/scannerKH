from django.db import models
from artikel.models import Artikel
from grosshaendler.models import Grosshaendler
from user.models import User
from datetime import datetime


class Position(models.Model):
    artikel = models.ForeignKey(Artikel, models.DO_NOTHING)
    menge = models.IntegerField(verbose_name='Menge')

    def __str__(self):
        return f"ARTIKEL: ({self.artikel.__str__()}), MENGE: {self.menge}"

class Bestellung(models.Model):
    grosshaendler = models.ForeignKey(Grosshaendler, on_delete=models.PROTECT)
    ersteller = models.ForeignKey(User, related_name='ersteller', on_delete=models.DO_NOTHING)
    erstellt = models.DateTimeField(default=datetime.now)
    bearbeiter = models.ForeignKey(User, related_name='bearbeiter', on_delete=models.DO_NOTHING)
    bearbeitet = models.DateTimeField(auto_now=True)
    uebertrager = models.ForeignKey(User, related_name='uebertrager', on_delete=models.DO_NOTHING)
    uebertragen = models.DateTimeField(blank=True, null=True)
    positionen = models.ManyToManyField(Position)

    def __str__(self):
        return f"GROßHÄNDLER: ({self.grosshaendler.__str__()}), ERSTELLT: {self.ersteller.__str__()} {self.erstellt.__str__()}, BEARBEITET: {self.bearbeiter.__str__()} {self.bearbeitet.__str__()}, ÜBERTRAGEN: {self.uebertrager.__str__()} {self.uebertragen.__str__()}\nPOSITIONEN: [{self.positionen}]"

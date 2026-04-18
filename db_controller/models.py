from django.db import models


class TrControl(models.Model):
    db_code = models.CharField(primary_key=True, max_length=100)
    showtext = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tr_control"

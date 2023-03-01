from django.db import models


class ActionStatistic(models.Model):
    session_key = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    count_of_visits = models.IntegerField()
    time_of_visit = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["session_key", "path"], name="Unique visit")]

from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=55)
    telegram = models.BigIntegerField(unique = True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "users"
        managed = False
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]

    def __str__(self):
        return self.name
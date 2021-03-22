from django.db import models


class SecureMessage(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    date_contacted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

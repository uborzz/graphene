from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField(help_text="Web URL of the site")
    description = models.TextField(blank=True)

from django.db import models


class Link(models.Model):
    url = models.TextField("User Link")
    email = models.CharField("Email", max_length=100)

    def __str__(self):
        return "{email}_{url}".format(email=self.email, url=self.url)

from celery import app, task
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction


class Link(models.Model):
    url = models.TextField("User Link")

    def __str__(self):
        return "{email}_{url}".format(email=self.email, url=self.url)


class UserEmail(models.Model):
    email = models.CharField("Email", max_length=100)
    url = models.ManyToManyField(Link)

    def __str__(self):
        return "{email}_{url}".format(email=self.email, url=self.url)


def link_email(email, url):
    try:
        instance = UserEmail.objects.get(email=email)
    except UserEmail.DoesNotExist:
        instance = UserEmail.objects.create(email=email)

    for item in url:
        try:
            current_url = Link.objects.get(url=item)
        except Link.DoesNotExist:
            current_url = Link.objects.create(url=item)
        instance.url.add(current_url)
    return instance

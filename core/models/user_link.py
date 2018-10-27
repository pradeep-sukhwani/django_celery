from celery import app, task
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class Link(models.Model):
    url = models.TextField("User Link")
    email = models.CharField("Email", max_length=100)

    def __str__(self):
        return "{email}_{url}".format(email=self.email, url=self.url)



@task()
def handle_save_task(instance_pk):
    try:
        instance = Link.objects.get(pk=instance_pk)
    except Link.DoesNotExist:
        pass


@receiver(post_save, sender=Link)
def my_model_post_save(sender, instance, **kwargs):
    transaction.on_commit(lambda: handle_save_task.apply_async(args=(instance.pk,)))

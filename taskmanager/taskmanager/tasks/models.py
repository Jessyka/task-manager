from django.db import models

class TaskManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            description__icontains=query
        )


class Task(models.Model):
    description = models.TextField('Tarefa')
    status = models.CharField('Status', max_length=100)
    date_created= models.DateTimeField('Data de criacao', auto_now_add=True)

    objects = TaskManager()
from django.db import models

# Create your models here.
class tadalist(models.Model):
    text = models.CharField(max_length=50)
    iscompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.text

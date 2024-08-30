from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.TextField()
    entry_date = models.DateField()
    taken_date = models.DateField(null=True, blank=True)
    item_came_from = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name
from django.db import models


class TodoList(models.Model):
    item = models.CharField(max_length=255, blank=True, null=True)
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'todo_list'

# Create your models here.

from django.db import models

# Create your models here.
OFFENCES = (
    ('RL', 'Late Reporting Time'),
    ('LONW', 'Learning Objective Not Written'),
    ('TNH', 'Teaching Not Happening'),
    ('CCN', 'No Class Control'),
    ('SMO', 'Students Moving Outside'),
    ('NHE', 'No Happiness Exercise'),
)

BLOCKS = (
    ('P', 'Primary'),
    ('M', 'Middle'),
    ('S', 'Senior'),
)

FLOORS = (
    ('G', 'Ground'),
    ('F', 'First'),
    ('S', 'Second'),
)


class Offence(models.Model):
    id = models.AutoField(primary_key=True, editable= False)
    date = models.DateTimeField(auto_now_add=True)
    block = models.CharField(max_length = 1,choices = BLOCKS)
    floor = models.CharField(max_length = 1,choices = FLOORS)
    period = models.CharField(max_length = 1)
    type = models.CharField(max_length = 4,choices = OFFENCES)
    grade = models.CharField(max_length = 2)
    section = models.CharField(max_length = 1)
    reporter = models.CharField(max_length=50, null=True,blank = True)

    def __str__(self):
        return str(self.date) + "-" + self.block + "-" + self.period +"-"+ self.type+"-"+ str(self.reporter)



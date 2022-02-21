from django.db import models

# Create your models here.
class Evaluation(models.Model):
    flname = models.CharField(max_length=100)
    sem = models.CharField(max_length=100)
    prof = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    subjectcode = models.CharField(max_length=100)

    mastery1 = models.IntegerField(blank=True, null=True)
    mastery2 = models.IntegerField(blank=True, null=True)
    mastery3 = models.IntegerField(blank=True, null=True)
    mastery4 = models.IntegerField(blank=True, null=True)
    mastery5 = models.IntegerField(blank=True, null=True)

    planning1 = models.IntegerField(blank=True, null=True)
    planning2 = models.IntegerField(blank=True, null=True)
    planning3 = models.IntegerField(blank=True, null=True)
    planning4 = models.IntegerField(blank=True, null=True)
    planning5 = models.IntegerField(blank=True, null=True)

    communication1 = models.IntegerField(blank=True, null=True)
    communication2 = models.IntegerField(blank=True, null=True)
    communication3 = models.IntegerField(blank=True, null=True)
    communication4 = models.IntegerField(blank=True, null=True)
    communication5 = models.IntegerField(blank=True, null=True)

    instructional1 = models.IntegerField(blank=True, null=True)
    instructional2 = models.IntegerField(blank=True, null=True)
    instructional3 = models.IntegerField(blank=True, null=True)
    instructional4 = models.IntegerField(blank=True, null=True)
    instructional5 = models.IntegerField(blank=True, null=True)

    classroom1 = models.IntegerField(blank=True, null=True)
    classroom2 = models.IntegerField(blank=True, null=True)
    classroom3 = models.IntegerField(blank=True, null=True)
    classroom4 = models.IntegerField(blank=True, null=True)
    classroom5 = models.IntegerField(blank=True, null=True)

    personal1 = models.IntegerField(blank=True, null=True)
    personal2 = models.IntegerField(blank=True, null=True)
    personal3 = models.IntegerField(blank=True, null=True)
    personal4 = models.IntegerField(blank=True, null=True)
    personal5 = models.IntegerField(blank=True, null=True)

    comments = models.CharField(max_length=1000)

class Average(models.Model):
    prof = models.CharField(max_length=100, blank=True, null=True)
    subjectcode = models.CharField(max_length=100, blank=True, null=True)
    mastery_average = models.DecimalField(max_digits=4, decimal_places=2)
    planning_average = models.DecimalField(max_digits=4, decimal_places=2)
    communication_average = models.DecimalField(max_digits=4, decimal_places=2)
    instructions_average =models.DecimalField(max_digits=4, decimal_places=2)
    classroom_average = models.DecimalField(max_digits=4, decimal_places=2)
    personal_average = models.DecimalField(max_digits=4, decimal_places=2)
    comment_average = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    Final_average = models.DecimalField(max_digits=4, decimal_places=2)
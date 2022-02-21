# Generated by Django 4.0.2 on 2022-02-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Average',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.CharField(blank=True, max_length=100, null=True)),
                ('subjectcode', models.CharField(blank=True, max_length=100, null=True)),
                ('mastery_average', models.DecimalField(decimal_places=2, max_digits=4)),
                ('planning_average', models.DecimalField(decimal_places=2, max_digits=4)),
                ('communication_average', models.DecimalField(decimal_places=2, max_digits=4)),
                ('instructions_average', models.DecimalField(decimal_places=2, max_digits=4)),
                ('classroom_average', models.DecimalField(decimal_places=2, max_digits=4)),
                ('personal_average', models.DecimalField(decimal_places=2, max_digits=4)),
                ('comment_average', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('Final_average', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flname', models.CharField(max_length=100)),
                ('sem', models.CharField(max_length=100)),
                ('prof', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('subjectcode', models.CharField(max_length=100)),
                ('mastery1', models.IntegerField(blank=True, null=True)),
                ('mastery2', models.IntegerField(blank=True, null=True)),
                ('mastery3', models.IntegerField(blank=True, null=True)),
                ('mastery4', models.IntegerField(blank=True, null=True)),
                ('mastery5', models.IntegerField(blank=True, null=True)),
                ('planning1', models.IntegerField(blank=True, null=True)),
                ('planning2', models.IntegerField(blank=True, null=True)),
                ('planning3', models.IntegerField(blank=True, null=True)),
                ('planning4', models.IntegerField(blank=True, null=True)),
                ('planning5', models.IntegerField(blank=True, null=True)),
                ('communication1', models.IntegerField(blank=True, null=True)),
                ('communication2', models.IntegerField(blank=True, null=True)),
                ('communication3', models.IntegerField(blank=True, null=True)),
                ('communication4', models.IntegerField(blank=True, null=True)),
                ('communication5', models.IntegerField(blank=True, null=True)),
                ('instructional1', models.IntegerField(blank=True, null=True)),
                ('instructional2', models.IntegerField(blank=True, null=True)),
                ('instructional3', models.IntegerField(blank=True, null=True)),
                ('instructional4', models.IntegerField(blank=True, null=True)),
                ('instructional5', models.IntegerField(blank=True, null=True)),
                ('classroom1', models.IntegerField(blank=True, null=True)),
                ('classroom2', models.IntegerField(blank=True, null=True)),
                ('classroom3', models.IntegerField(blank=True, null=True)),
                ('classroom4', models.IntegerField(blank=True, null=True)),
                ('classroom5', models.IntegerField(blank=True, null=True)),
                ('personal1', models.IntegerField(blank=True, null=True)),
                ('personal2', models.IntegerField(blank=True, null=True)),
                ('personal3', models.IntegerField(blank=True, null=True)),
                ('personal4', models.IntegerField(blank=True, null=True)),
                ('personal5', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
    ]

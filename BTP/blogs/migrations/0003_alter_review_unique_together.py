# Generated by Django 4.0.1 on 2022-11-13 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_review'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
    ]

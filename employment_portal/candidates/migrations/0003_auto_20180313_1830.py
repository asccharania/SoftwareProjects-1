# Generated by Django 2.0.1 on 2018-03-13 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_auto_20180313_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='bio',
            new_name='bio1',
        ),
    ]

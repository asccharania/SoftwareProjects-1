# Generated by Django 2.0.1 on 2018-03-12 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_solicit', '0015_auto_20180312_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_invitation',
            name='uuid',
            field=models.CharField(default='PBJ9M', max_length=5, primary_key=True, serialize=False),
        ),
    ]

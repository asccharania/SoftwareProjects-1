# Generated by Django 2.0.1 on 2018-03-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_solicit', '0010_auto_20180312_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_invitation',
            name='uuid',
            field=models.CharField(default='GNCSJ', max_length=5, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.0.2 on 2018-03-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer_solicit', '0018_auto_20180316_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_invitation',
            name='uuid',
            field=models.CharField(default='TKUE8', max_length=5, primary_key=True, serialize=False),
        ),
    ]
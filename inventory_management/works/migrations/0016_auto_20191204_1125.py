# Generated by Django 2.0.8 on 2019-12-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0015_auto_20191007_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='jc_number',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='po_number',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

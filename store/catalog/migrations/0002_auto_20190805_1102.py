# Generated by Django 2.2.4 on 2019-08-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]

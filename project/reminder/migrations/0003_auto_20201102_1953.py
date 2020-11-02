# Generated by Django 3.0.7 on 2020-11-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_auto_20201102_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='warning_event',
            field=models.IntegerField(choices=[(0, 'Always'), (1, 'Raining tomorrow'), (2, 'Snowing tomorrow'), (3, 'Temperature dropping by 3 F '), (4, 'Temperature rising by 3 F')], default=0),
        ),
    ]

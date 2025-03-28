# Generated by Django 5.1.6 on 2025-03-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_fixedlecture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturehall',
            name='projector',
        ),
        migrations.AddField(
            model_name='lecturehall',
            name='ac_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='lecturehall',
            name='projector_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='lecturehall',
            name='capacity',
            field=models.PositiveIntegerField(),
        ),
    ]

# Generated by Django 5.1.6 on 2025-03-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_booking_ac_required_booking_price_and_more'),
        ('timetable', '0004_lecturehall_non_ac_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='time_slot',
        ),
        migrations.AddField(
            model_name='booking',
            name='time_slots',
            field=models.ManyToManyField(to='timetable.timeslot'),
        ),
    ]

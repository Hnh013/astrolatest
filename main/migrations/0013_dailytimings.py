# Generated by Django 3.0 on 2020-07-21 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_hindumonthyear'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTimings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rahu_from', models.TimeField()),
                ('rahu_to', models.TimeField()),
                ('yama_from', models.TimeField()),
                ('yama_to', models.TimeField()),
                ('gulika_from', models.TimeField()),
                ('gulika_to', models.TimeField()),
                ('abhi_from', models.TimeField()),
                ('abhi_to', models.TimeField()),
                ('astroprofile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Astro_Profile')),
            ],
        ),
    ]

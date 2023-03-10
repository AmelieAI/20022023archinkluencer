# Generated by Django 4.1.6 on 2023-02-08 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Archinkluencer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="modeldataifc",
            name="doorpos",
            field=models.CharField(default=django.utils.timezone.now, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="modeldataifc",
            name="length",
            field=models.CharField(default=django.utils.timezone.now, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="modeldataifc",
            name="wallname",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="modeldataifc",
            name="wallname_wc",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="modeldataifc",
            name="door",
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name="modeldataifc",
            name="name",
            field=models.CharField(max_length=6),
        ),
    ]

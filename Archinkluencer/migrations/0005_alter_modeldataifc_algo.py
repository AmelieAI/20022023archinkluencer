# Generated by Django 4.1.6 on 2023-02-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Archinkluencer", "0004_alter_modeldataifc_algo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modeldataifc",
            name="algo",
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 4.1.dev20220404083157 on 2022-04-20 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer", old_name="customer", new_name="manager",
        ),
    ]

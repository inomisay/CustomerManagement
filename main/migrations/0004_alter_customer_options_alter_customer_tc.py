# Generated by Django 4.1.dev20220404083157 on 2022-04-20 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_customer_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer", options={"ordering": ["-created_at"]},
        ),
        migrations.AlterField(
            model_name="customer",
            name="tc",
            field=models.CharField(
                max_length=11,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "\\d{11,11}", "Number must be 11 digits", "Invalid number"
                    )
                ],
            ),
        ),
    ]

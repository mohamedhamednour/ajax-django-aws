# Generated by Django 5.2 on 2025-05-01 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subcategory",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subcategories",
                to="productapp.category",
            ),
        ),
    ]

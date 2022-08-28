# Generated by Django 4.1 on 2022-08-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0006_alter_purchase_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
    ]

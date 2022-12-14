# Generated by Django 4.1 on 2022-08-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0017_rename_item_stock_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="box",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="stock",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=8, null=True
            ),
        ),
    ]

# Generated by Django 4.1 on 2022-08-24 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_rename_item_name_item_itemname"),
        ("stocks", "0012_rename_boxes_sale_boxes_out_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("boxes", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="items.item"
                    ),
                ),
            ],
        ),
    ]

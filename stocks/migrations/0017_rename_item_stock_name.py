# Generated by Django 4.1 on 2022-08-27 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0016_remove_stock_items_stock_box_stock_item_stock_price"),
    ]

    operations = [
        migrations.RenameField(model_name="stock", old_name="item", new_name="name",),
    ]

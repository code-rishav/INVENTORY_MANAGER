# Generated by Django 4.1 on 2022-08-23 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0007_alter_purchase_price"),
    ]

    operations = [
        migrations.RemoveField(model_name="purchase", name="price",),
    ]

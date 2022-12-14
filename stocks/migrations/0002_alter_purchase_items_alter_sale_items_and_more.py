# Generated by Django 4.1 on 2022-08-23 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0001_initial"),
        ("stocks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="items",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="items.item"
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="items",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="items.item"
            ),
        ),
        migrations.AlterField(
            model_name="stocks",
            name="items",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="items.item"
            ),
        ),
    ]

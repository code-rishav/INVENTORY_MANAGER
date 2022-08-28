# Generated by Django 4.1 on 2022-08-28 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_amount_status_amount"),
    ]

    operations = [
        migrations.RenameField(
            model_name="amount_lended",
            old_name="Amount_Lended",
            new_name="amount_lended",
        ),
        migrations.RenameField(
            model_name="amount_lended", old_name="Date", new_name="date",
        ),
        migrations.RenameField(
            model_name="amount_lended", old_name="Store_Name", new_name="store_name",
        ),
        migrations.RenameField(
            model_name="amount_received",
            old_name="Amount_Received",
            new_name="amount_received",
        ),
        migrations.RenameField(
            model_name="amount_received", old_name="Date", new_name="date",
        ),
        migrations.RenameField(
            model_name="amount_received", old_name="Store_Name", new_name="store_name",
        ),
        migrations.RenameField(
            model_name="amount_status", old_name="Store_name", new_name="store_name",
        ),
        migrations.RenameField(
            model_name="customer", old_name="Contact_No", new_name="contact_no",
        ),
        migrations.RenameField(
            model_name="customer", old_name="GST_IN", new_name="gst_in",
        ),
        migrations.RenameField(
            model_name="customer", old_name="PAN_CARD", new_name="pan_card",
        ),
        migrations.RenameField(
            model_name="customer", old_name="Store_Name", new_name="store_name",
        ),
    ]

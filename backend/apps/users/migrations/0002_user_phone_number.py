# Generated by Django 4.1.4 on 2023-01-21 14:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="+923008999222",
                max_length=30,
                region=None,
                verbose_name="Phone Number",
            ),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.2.6 on 2019-10-10 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"permissions": (("reset_user_password", "Reset Password"),)},
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_stages_email", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="emailstage", name="ssl_certfile",),
        migrations.RemoveField(model_name="emailstage", name="ssl_keyfile",),
        migrations.AddField(
            model_name="emailstage",
            name="token_expiry",
            field=models.IntegerField(
                default=30, help_text="Time in minutes the token sent is valid."
            ),
        ),
    ]

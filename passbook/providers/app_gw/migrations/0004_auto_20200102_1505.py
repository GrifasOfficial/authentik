# Generated by Django 2.2.9 on 2020-01-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_providers_app_gw", "0003_applicationgatewayprovider"),
    ]

    operations = [
        migrations.RenameField(
            model_name="applicationgatewayprovider",
            old_name="host",
            new_name="external_host",
        ),
        migrations.AddField(
            model_name="applicationgatewayprovider",
            name="internal_host",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]

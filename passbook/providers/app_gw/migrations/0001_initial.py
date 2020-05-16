# Generated by Django 2.2.6 on 2019-10-07 14:07

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("passbook_core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApplicationGatewayProvider",
            fields=[
                (
                    "provider_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="passbook_core.Provider",
                    ),
                ),
                (
                    "server_name",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(), size=None
                    ),
                ),
                (
                    "upstream",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(), size=None
                    ),
                ),
                ("enabled", models.BooleanField(default=True)),
                (
                    "authentication_header",
                    models.TextField(blank=True, default="X-Remote-User"),
                ),
                (
                    "default_content_type",
                    models.TextField(default="application/octet-stream"),
                ),
                ("upstream_ssl_verification", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Application Gateway Provider",
                "verbose_name_plural": "Application Gateway Providers",
            },
            bases=("passbook_core.provider",),
        ),
        migrations.CreateModel(
            name="RewriteRule",
            fields=[
                (
                    "propertymapping_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="passbook_core.PropertyMapping",
                    ),
                ),
                ("match", models.TextField()),
                ("halt", models.BooleanField(default=False)),
                ("replacement", models.TextField()),
                (
                    "redirect",
                    models.CharField(
                        choices=[
                            ("internal", "Internal"),
                            (301, "Moved Permanently"),
                            (302, "Found"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "conditions",
                    models.ManyToManyField(blank=True, to="passbook_core.Policy"),
                ),
            ],
            options={
                "verbose_name": "Rewrite Rule",
                "verbose_name_plural": "Rewrite Rules",
            },
            bases=("passbook_core.propertymapping",),
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-12 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("passbook_flows", "0005_auto_20200512_1158"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserDeleteStage",
            fields=[
                (
                    "stage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="passbook_flows.Stage",
                    ),
                ),
            ],
            options={
                "verbose_name": "User Delete Stage",
                "verbose_name_plural": "User Delete Stages",
            },
            bases=("passbook_flows.stage",),
        ),
    ]

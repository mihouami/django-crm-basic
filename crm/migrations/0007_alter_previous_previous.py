# Generated by Django 5.0.2 on 2024-02-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crm", "0006_alter_previous_previous"),
    ]

    operations = [
        migrations.AlterField(
            model_name="previous",
            name="previous",
            field=models.URLField(blank=True, null=True),
        ),
    ]

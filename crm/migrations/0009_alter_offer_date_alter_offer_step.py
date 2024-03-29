# Generated by Django 5.0.2 on 2024-02-21 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crm", "0008_offer_delete_previous_alter_company_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="offer",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="offer",
            name="step",
            field=models.CharField(
                choices=[
                    ("RFQ", "RFQ"),
                    ("Offer", "Offer"),
                    ("Negotiation", "Negotiation"),
                    ("Won", "Won"),
                    ("Lost", "Lost"),
                ],
                max_length=11,
            ),
        ),
    ]

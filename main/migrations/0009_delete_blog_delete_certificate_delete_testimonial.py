# Generated by Django 4.2 on 2023-04-14 18:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_portfolio_date"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Blog",
        ),
        migrations.DeleteModel(
            name="Certificate",
        ),
        migrations.DeleteModel(
            name="Testimonial",
        ),
    ]

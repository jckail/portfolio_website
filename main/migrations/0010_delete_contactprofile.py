# Generated by Django 4.2 on 2023-04-14 21:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_delete_blog_delete_certificate_delete_testimonial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ContactProfile",
        ),
    ]
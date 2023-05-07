# Generated by Django 4.2 on 2023-05-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("myapp", "0008_delete_product_delete_react"),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio",
            fields=[
                ("name", models.CharField(max_length=255)),
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("data", models.JSONField(default=list)),
            ],
        ),
    ]

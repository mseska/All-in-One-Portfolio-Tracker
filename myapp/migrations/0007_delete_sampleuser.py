# Generated by Django 4.2 on 2023-04-19 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_sampleuser"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SampleUser",
        ),
    ]

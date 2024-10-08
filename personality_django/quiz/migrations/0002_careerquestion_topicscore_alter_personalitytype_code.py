# Generated by Django 4.2.13 on 2024-07-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CareerQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topic", models.CharField(max_length=50)),
                ("question", models.TextField()),
                ("options", models.TextField()),
                ("answer", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="TopicScore",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topic", models.CharField(max_length=50)),
                ("score", models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name="personalitytype",
            name="code",
            field=models.CharField(max_length=5, unique=True),
        ),
    ]

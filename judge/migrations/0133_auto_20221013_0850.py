# Generated by Django 2.2.25 on 2022-10-13 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0132_auto_20220915_1349"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContestProblemClarification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(verbose_name="clarification body")),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="clarification timestamp"
                    ),
                ),
                (
                    "problem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="judge.ContestProblem",
                        verbose_name="clarified problem",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ProblemClarification",
        ),
    ]

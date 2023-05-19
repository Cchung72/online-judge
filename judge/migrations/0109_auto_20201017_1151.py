# Generated by Django 2.2.12 on 2020-10-17 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0108_submission_judged_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="html_link",
            field=models.TextField(
                default="",
                max_length=1000,
                verbose_name="html link to comments, used for non-comments",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="comment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="judge.Comment",
                verbose_name="comment",
            ),
        ),
    ]

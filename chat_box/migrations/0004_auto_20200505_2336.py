# Generated by Django 2.2.12 on 2020-05-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_box', '0003_auto_20200505_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='is hidden'),
        ),
    ]
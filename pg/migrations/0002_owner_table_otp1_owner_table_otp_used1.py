# Generated by Django 4.1 on 2023-03-03 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_table',
            name='otp1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='owner_table',
            name='otp_used1',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
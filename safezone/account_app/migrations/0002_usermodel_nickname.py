# Generated by Django 4.1.5 on 2023-06-12 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='nickname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
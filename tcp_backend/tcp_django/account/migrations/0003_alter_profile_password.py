# Generated by Django 5.0.7 on 2024-08-09 03:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_profile_password_alter_accountlogintype_logintype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="password",
            field=models.CharField(default=None, max_length=64, null=True),
        ),
    ]

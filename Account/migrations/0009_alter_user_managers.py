# Generated by Django 4.2.6 on 2024-04-11 08:41

import Account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_remove_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', Account.models.CustomUserManager()),
            ],
        ),
    ]

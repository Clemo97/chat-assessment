# Generated by Django 4.1.2 on 2022-10-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userquery_urgency_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquery',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.8 on 2024-01-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_email_verify_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='free_models_count',
            field=models.IntegerField(default=2),
        ),
    ]

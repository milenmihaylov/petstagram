# Generated by Django 3.2.12 on 2023-05-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstagram_auth', '0002_petstagramuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 3.2.12 on 2023-04-19 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_auto_20230419_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('parrot', 'Parrot'), ('snake', 'Snake'), ('rabbit', 'Rabbit')], max_length=6),
        ),
    ]

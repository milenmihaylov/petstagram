# Generated by Django 3.2.12 on 2023-04-26 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('petstagram_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('name', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('picture', models.ImageField(blank=True, upload_to='images/accounts')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='petstagram_auth.petstagramuser')),
            ],
        ),
    ]

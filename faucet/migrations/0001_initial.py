# Generated by Django 2.0.2 on 2018-03-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaucetTransaction',
            fields=[
                ('public_key', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('transfered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

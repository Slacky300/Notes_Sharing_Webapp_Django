# Generated by Django 4.1.7 on 2023-03-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0017_alter_notes_ndetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='coins_scored',
            field=models.FloatField(default=0),
        ),
    ]